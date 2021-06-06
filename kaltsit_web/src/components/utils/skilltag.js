/* skill-tag */
/* 缺 key: cost, base_atk_time, time, talent_scale, prob, sluggish
ability_range_forward_extend
attack@ (range_scale, prob, stun, max_target, duration, mobve_speed
*/
// 属性增加 key: atk, def, max_hp
function paramUp (basedata, upValue) {
  return basedata * (1 + upValue)
}
// 攻速增加 key: atk_speed
function atkSpdUp (basedata, upValue) {
  return basedata * 100 / (100 + upValue)
}
// Scale（瞬时生效）key: atk_scale, heal_scale
function scaleUp (basedata, scaleValue) {
  return basedata * scaleValue
}