// 用于文本颜色
// 描述
function descTranslate (str, blackboard) {
  str = tagTranslate(str)
  str = completeValue(str, blackboard)
  return str
}
// 标签转化
function tagTranslate (str) {
  str = str.replace(/<@ba.vup>/g, '<span class="vup">')
  str = str.replace(/<@ba.rem>/g, '<span class="rem">')
  str = str.replace(/<@ba.vdown>/g, '<span class="vdown">')
  str = str.replace(/\\n/g, '<br>')
  str = str.replace(/<\/>/g, '</span>')
  return str
}
// 技能内容补充
function completeValue (str, blackboard) {
  for (const i in blackboard) {
    console.log(blackboard[i].key)
    console.log(blackboard[i].value)
    str = valueFormat(str, blackboard[i].key, blackboard[i].value)
  }
  return str
}
// format()
// 字符串, 匹配值, 替换项
function valueFormat (str, key, param) {
  str = str.replace('{' + key + '}', param)
  str = str.replace('{' + key.toUpperCase() + '}', param)
  str = str.replace('{' + key + ':0%}', parseInt(param * 100) + '%')
  str = str.replace('{' + key.toUpperCase() + ':0.0%}', (param * 100).toFixed(1) + '%')
  str = str.replace('{' + key + ':0}', parseInt(param))
  str = str.replace('{' + key + ':0.0}', param.toFixed(1))
  str = str.replace('{-' + key + '}', -param)
  str = str.replace('{-' + key + ':0%}', -parseInt(param * 100) + '%')
  return str
}
module.exports = {
  descTranslate
}
