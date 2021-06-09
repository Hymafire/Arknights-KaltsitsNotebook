/* eslint-disable camelcase */
// 攻击类计算
// 秒伤 per-damage =============================
// 攻击，攻击间隔，伤害类型，攻击方式
function perDamage (param, pretData) {
  const atk = param.atk
  const atkTime = param.atkTime
  const baseAtkTime = param.baseAtkTime
  const damMod = pretData.damMod
  const atkMod = pretData.atkMod
  // damMod
  const data = []
  if (damMod === 'Phy') {
    perDamagePhy(data, atk, atkTime, baseAtkTime)
  } else if (damMod === 'Mag') {
    perDamageMag(data, atk, atkTime, baseAtkTime)
  }
  // atkMod
  if (atkMod === 3) {
    for (let i = 0; i < data.length; i++) {
      data[i][1] *= 2
    }
  } else if (atkMod === 4) {
    for (let i = 0; i < data.length; i++) {
      data[i][1] *= 0.8
    }
  }
  return data
}
// 物理
function perDamagePhy (data, atk, atkTime, baseAtkTime) {
  for (let def = 0; def <= 1000; def++) {
    const damage = Math.max(atk - def, atk * 0.05)
    const per_damage = (damage / atkTime) * (baseAtkTime / 100)
    data.push([def, per_damage])
  }
  return data
}
// 法术
function perDamageMag (data, atk, atkTime, baseAtkTime) {
  for (let resMag = 0; resMag <= 100; resMag++) {
    const damage = Math.max(atk * (1 - resMag / 100), atk * 0.05)
    const per_damage = (damage / atkTime) * (baseAtkTime / 100)
    data.push([resMag, per_damage])
  }
  return data
}
// 真伤、治疗
/*
function perDamageTruthOrHeal (data, atk, atkTime, baseAtkTime) {
  return atk / atkTime
}
*/
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
module.exports = {
  perDamage,
  atkModJudge,
  damModJudge
}
