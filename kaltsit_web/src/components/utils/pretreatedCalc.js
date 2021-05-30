/* 预处理组件 */
/* 参数输入、结果输出 */
function emDataPretreate (preData) {
  const paramList = ['atk', 'def', 'maxHp', 'magRes', 'atkTime', 'perDam', 'range']
  const classList = ['profession', 'position', 'rarity']
  const professionList = ['CASTER', 'MEDIC', 'WARRIOR', 'SUPPORT', 'SNIPER', 'TANK', 'PIONEER', 'SPECIAL']
  const positionList = ['MELEE', 'RANGED']
  const rarityList = [0, 1, 2, 3, 4, 5]
  const baseList = [professionList, positionList, rarityList]
  const pretreatedData = initParamStruct(paramList, classList, baseList)
  //
  for (const emKey in preData) {
    const employee = preData[emKey]
    for (const param in pretreatedData) {
      for (const class_ in pretreatedData[param]) {
        if (['atk', 'def', 'maxHp'].includes(param)) {
          const value = employee.phases[param][employee.phases[param].length - 1][1] + employee.favor[param]
          if (class_ === 'totalAvg') {
            const obj = pretreatedData[param].totalAvg
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          } else {
            const obj = pretreatedData[param][class_][employee[class_]]
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          }
        } else if (param === 'magRes') {
          const value = employee.phases[param][employee.phases[param].length - 1]
          if (class_ === 'totalAvg') {
            const obj = pretreatedData[param].totalAvg
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          } else {
            const obj = pretreatedData[param][class_][employee[class_]]
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          }
        } else if (param === 'atkTime') {
          const value = employee.phases[param]
          if (class_ === 'totalAvg') {
            const obj = pretreatedData[param].totalAvg
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          } else {
            const obj = pretreatedData[param][class_][employee[class_]]
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          }
        } else if (param === 'perDam') {
          const value = (employee.phases.atk[employee.phases.atk.length - 1][1] + employee.favor.atk) / employee.phases.atkTime
          if (class_ === 'totalAvg') {
            const obj = pretreatedData[param].totalAvg
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          } else {
            const obj = pretreatedData[param][class_][employee[class_]]
            obj.emNum++
            obj.sumValue += value
            obj.maxValue = Math.max(obj.maxValue, value)
            obj.minValue = Math.min(obj.minValue, value)
          }
        }
      }
    }
  }
  // 平均值
  for (const param in pretreatedData) {
    for (const class_ in pretreatedData[param]) {
      if (param !== 'range') {
        if (class_ === 'totalAvg') {
          const obj = pretreatedData[param].totalAvg
          obj.avgValue = obj.sumValue / obj.emNum
        } else {
          for (const base in pretreatedData[param][class_]) {
            const obj = pretreatedData[param][class_][base]
            obj.avgValue = obj.sumValue / obj.emNum
          }
        }
      }
    }
  }
  return pretreatedData
}
// 初始化结构
// 干员结构
function initBaseStruct (baseList) {
  const baseObj = {}
  for (const i in baseList) {
    baseObj[baseList[i]] = {
      emNum: 0,
      sumValue: 0,
      avgValue: null,
      maxValue: -Infinity,
      minValue: Infinity
    }
  }
  return baseObj
}
function initClassStruct (classList, baseList) {
  const classObj = {}
  for (const i in classList) {
    classObj[classList[i]] = initBaseStruct(baseList[i])
  }
  classObj.totalAvg = {
    emNum: 0,
    sumValue: 0,
    avgValue: null,
    maxValue: -Infinity,
    minValue: Infinity
  }
  return classObj
}
function initParamStruct (paramList, classList, baseList) {
  const paramObj = {}
  for (const i in paramList) {
    paramObj[paramList[i]] = initClassStruct(classList, baseList)
  }
  return paramObj
}
/* ================================================== */
module.exports = {
  emDataPretreate
}
