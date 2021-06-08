/* skillParamCalc */
// 入口
function getSkillParam (emParam, skillData, skillType) {
  const skillParam = JSON.parse(JSON.stringify(emParam))
  if (skillType === 'dam') {
    damCalcMod(skillParam, skillData)
  }
  return skillParam
}
// dam
function damCalcMod (skillParam, skillData) {
  for (let i = 0; i < skillData.blackboard.length; i++) {
    const calcKey = skillData.blackboard[i].key
    const calcValue = skillData.blackboard[i].value
    if (calcKey === 'atk') {
      skillParam.atk = paramUp(skillParam.atk, calcValue)
    } else if (calcKey === 'atk_speed') {
      skillParam.atkTime = atkSpdUp(skillParam.atkTime, calcValue)
    } else if (calcKey === 'atk_scale') {
      skillParam.atk = scaleUp(skillParam.atk, calcValue)
    }
  }
  return skillParam
}
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
  return basedata + upValue
}
// Scale（瞬时生效）key: atk_scale, heal_scale
function scaleUp (basedata, scaleValue) {
  return basedata * scaleValue
}
// ==================================
module.exports = {
  getSkillParam
}
