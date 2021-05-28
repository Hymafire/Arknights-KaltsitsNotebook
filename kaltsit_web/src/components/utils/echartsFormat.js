/* 格式化输入Echars的数据 */
// 格式化 Title, xAxis, yAxis Label
function labelFormat (xAxis, yAxis) {
  const echartLabel = []
  echartLabel[0] = yAxis + '-' + xAxis
  echartLabel[1] = xAxis
  echartLabel[2] = yAxis
  return echartLabel
}
/* ======================= 折线图 ======================== */
// 格式化数据
function lineSeriesFormat (dataList, nameList) {
  const seriesList = []
  for (const i in dataList) {
    const Obj = {
      name: nameList[i],
      type: 'line',
      showSymbol: false,
      clip: true,
      data: dataList[i]
    }
    seriesList.push(Obj)
  }
  return seriesList
}
module.exports = {
  labelFormat,
  lineSeriesFormat
}
