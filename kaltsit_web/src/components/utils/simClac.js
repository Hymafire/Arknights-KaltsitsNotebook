// 基础计算函数
// 秒输出量
function preAttack (atk, atkspd, baseatkt, def, magres, dammod) {
  const dam = damage(atk, def, magres, dammod)
  return dam * atkspd / baseatkt
}
// 最终单次伤害量
function damage (atk, def, magres, dammod) {
  if (dammod === 'Phy') {
    return Math.max(atk * 0.05, atk - def)
  } else if (dammod === 'Mag') {
    return Math.max(atk * 0.05, atk * (100 - magres) / 100)
  } else {
    return atk
  }
}
