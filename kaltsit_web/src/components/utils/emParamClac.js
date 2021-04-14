/* eslint-disable camelcase */
// 用于计算干员的基础属性
function getEmployeeParam (name, table, elite, level, favor) {
  const em_data = getEmployeeData(name, table)
  var em_param1 = employeeBaseParamClac(em_data, elite, level)
  var em_param2 = employeeFavorClac(em_data, em_param1, favor)
  // 潜能
  // 天赋
  return em_param2
}
// 用于读取干员的数据
function getEmployeeData (name, table) {
  for (var em in table) {
    if (table[em].name === name) {
      return table[em]
    }
  }
}
// 用于计算干员的等级数据
function employeeBaseParamClac (em_data, elite, level) {
  const max_data = em_data.parse[elite].attributesKeyFrames[1].data
  const min_data = em_data.parse[elite].attributesKeyFrames[0].data
  const diff = em_data.parse[elite].maxLevel - 1
  var level_data = min_data
  // 具体参数计算
  level_data.maxHp = Math.round(level_data.maxHp + (level - 1) * (max_data.maxHp - min_data.maxHp) / diff)
  level_data.atk = Math.round(level_data.atk + (level - 1) * (max_data.atk - min_data.atk) / diff)
  level_data.def = Math.round(level_data.def + (level - 1) * (max_data.def - min_data.def) / diff)
  level_data.magicResistance = Math.round(level_data.magicResistance + (level - 1) * (max_data.magicResistance - min_data.magicResistance) / diff)
  return level_data
}
// 用于计算信赖的加成
function employeeFavorClac (em_data, em_param, favor) {
  const min_favor = Math.min(favor, 100)
  const favor_data = em_data.favorKeyFrames[1].data
  em_param.maxHp = Math.round(em_param.maxHp + favor_data * min_favor / 100)
  em_param.atk = Math.round(em_param.atk + favor_data * min_favor / 100)
  em_param.def = Math.round(em_param.def + favor_data * min_favor / 100)
  em_param.magicResistance = Math.round(em_param.magicResistance + favor_data * min_favor / 100)
  return em_param
}
