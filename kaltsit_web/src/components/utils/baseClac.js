// 计算工具库
// 等级
function baseParamClac (param, data, input) {
  const Lv = input.levelValue - 1
  const elt = input.elite
  const diff = data.maxLevel[elt] - 1
  //
  param.maxHp = data.maxHp[elt][0] + Math.round(Lv * (data.maxHp[elt][1] - data.maxHp[elt][0]) / diff)
  param.atk = data.atk[elt][0] + Math.round(Lv * (data.atk[elt][1] - data.atk[elt][0]) / diff)
  param.def = data.def[elt][0] + Math.round(Lv * (data.def[elt][1] - data.def[elt][0]) / diff)
  param.magRes = data.magRes[elt]
  param.cost = data.cost[elt]
  param.blockCnt = data.blockCnt[elt]
  param.range = data.range[elt]
  param.atkTime = data.atkTime
  param.baseAtkTime = 100.0
  param.respawnTime = data.respawnTime
  //
  return param
}
// 信赖
function favorClac (param, favorData, favor) {
  param.maxHp += Math.round(favorData.maxHp * favor / 100)
  param.atk += Math.round(favorData.atk * favor / 100)
  param.def += Math.round(favorData.def * favor / 100)
  return param
}
// 潜能
function potentialClac (param, potentialData, potential) {
  for (let i = 0; i < potential; i++) {
    const data = potentialData[i]
    if (data.type === 0) {
      param[data.attType] += data.value
    }
  }
}
// 天赋
function talentClac () {
  console.log('aaa')
}
//
module.exports = {
  baseParamClac,
  favorClac,
  potentialClac,
  talentClac
}
