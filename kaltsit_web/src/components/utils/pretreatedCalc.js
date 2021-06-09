/* 预处理组件 */
/* ====================== employee ================== */
function emTablePretreate (preData) {
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
/* ==================== em ===================== */
function emDataPretreate (preData, skillsData) {
  const emPreObj = {}
  emPreObj.atkMod = atkModJudge(preData.description)
  emPreObj.damMod = damModJudge(preData.description)
  for (const skill in skillsData) {
    const skillObj = {}
    skillObj.damMod = emPreObj.damMod
    skillObj.atkMod = emPreObj.atkMod
    emPreObj[skill] = skillObj
  }
  return emPreObj
}
// 判断攻击类型
// atkMod: 0-普通, 1-群攻, 2-有限群攻, 3-双击, 4-远程降攻
function atkModJudge (description) {
  let atkMod = 0
  if (description.indexOf('群体') !== -1) {
    atkMod = 1
  } else if (description.indexOf('所有敌人') !== -1) {
    atkMod = 2
  } else if (description.indexOf('两次') !== -1) {
    atkMod = 3
  } else if (description.indexOf('远程攻击') !== -1) {
    atkMod = 4
  }
  return atkMod
}
// 判断伤害类型
// damMod: Phy-物理，Mag-法术，Heal-治疗，True-真实，NoAtk-不攻击
function damModJudge (description) {
  let damMod = 'Phy'
  if (description.indexOf('法术') !== -1) {
    damMod = 'Mag'
  } else if (description.indexOf('恢复') !== -1) {
    damMod = 'Heal'
  } else if (description.indexOf('真实') !== -1) {
    damMod = 'True'
  } else if (description.indexOf('不攻击') !== -1) {
    damMod = 'NoAtk'
  }
  return damMod
}
/* ================================================ */
module.exports = {
  emTablePretreate,
  emDataPretreate
}
