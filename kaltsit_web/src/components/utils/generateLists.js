/**
 * Generate EmployeeList and EnemyList
 */

function generateEmployeeList (emTable, local) {
  // const emProf = require('../../assets/locales/prof_list.json')[local]
  const employeeList = []
  return employeeList
}

function generateEnemyList (enTable, local) {
  const enLevel = require('../../assets/locales/enLevel_list.json')[local]
  const enemyList = []
  const enemyChiList = { NORMAL: [], ELITE: [], BOSS: [] }
  for (const en in enTable) {
    const enemyChiDict = {}
    enemyChiDict.name = enTable[en].name
    try {
      enemyChiList[enTable[en].enemyLevel].push(enemyChiDict)
    } catch {
    }
  }
  for (const level in enLevel) {
    const enemyChiDict = {
      name: enLevel[level],
      children: enemyChiList[level]
    }
    enemyList.push(enemyChiDict)
  }
  return enemyList
}

module.exports = {
  generateEmployeeList,
  generateEnemyList
}
