/* eslint-disable camelcase */
// 攻击类计算
// 秒伤 per-damage =============================
// 攻击，攻击间隔，伤害类型，攻击方式
function perDamage (atk, atkTime, damMod, atkMod) {
  // damMod
  const data = []
  if (damMod === 'Phy') {
    perDamagePhy(data, atk, atkTime)
  } else if (damMod === 'Mag') {
    perDamageMag(data, atk, atkTime)
  }
  // atkMod
  if (atkMod === '3') {
    for (let i = 0; i < data.length; i++) {
      data[i][1] *= 2
    }
  } else if (atkMod === '4') {
    for (let i = 0; i < data.length; i++) {
      data[i][1] *= 0.8
    }
  }
  return data
}
// 物理
function perDamagePhy (data, atk, atkTime) {
  for (let def = 0; def <= 1000; def++) {
    const damage = Math.max(atk - def, atk * 0.05)
    const per_damage = damage / atkTime
    data.push([def, per_damage])
  }
  return data
}
// 法术
function perDamageMag (data, atk, atkTime) {
  for (let resMag = 0; resMag <= 100; resMag++) {
    const damage = Math.max(atk * (1 - resMag / 100), atk * 0.05)
    const per_damage = damage / atkTime
    data.push([resMag, per_damage])
  }
  return data
}
// 真伤、治疗
/*
function perDamageTruthOrHeal (atk, atkTime) {
  return atk / atkTime
}
*/
//
module.exports = {
  perDamage
}
