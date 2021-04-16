# 此组件用于将初始的解包数据转换成 kaltsit-web 所需要的网页数据
# 使用方法 直接调用本组件

import json

#=============================================================================================#
#===================================== 用于敌方数据的转换 =======================================#
class EnemyDataSwitch(object):

    # 初始化参数
    def __init__(self):
        self.data_json = {}             # 基础数据 enemy_database.json
        self.handbook_json = {}         # 描述数据 enemy_handbook_table.json
        self.enemy_data = {}            # 敌方参数 (kaltsit-web/enemy 展示数据)
        self.enemy_list = {}            # 敌方列表 (kaltsit-web/enemy 树形控件:data参数)

    # 入口函数 
    def letsEnemySwitch(self):
        self.getJsonData()
        self.getEnemyData()
        self.getEnemyList()

    #========= 获取原始的json文件: enemy_database.json, enemy_handbook_table.json ========#
    def getJsonData(self):
        # 获取 enemy_database.json
        with open("enemy_database.json", encoding="utf-8") as f:
            self.data_json = json.load(f)        
        # 获取 enemy_handbook_table.json
        with open("enemy_handbook_table.json", encoding="utf-8") as f:
            self.handbook_json = json.load(f)

    #============ 处理 enemy_database.json, enemy_handbook_table.json 的数据 ============#

    # 生成敌方列表 enemylist.json
    # enemyLevel: NORMAL, ELITE, BOSS
    def getEnemyList(self):
        #for em in self.handbook_json:
            #print(em)
        pass
        
    # 生成敌方数据 enemydata.json
    def getEnemyData(self):
        for em in self.data_json["enemies"]:
            tmp_key = em["Key"]
            level = len(em["Value"])            
            base_data = {}    # 基数据
            # 提取数据（不变的）
            # 除去：level, prefabKey, cost, blockCnt, attackSpeed, respawnTime, maxDeployCount
            tmp_data = em["Value"][0]["enemyData"]    # 参数重定位
            base_data["Key"] = tmp_key
            base_data["name"] = tmp_data["name"]["m_value"]
            base_data["description"] = tmp_data["description"]["m_value"]
            base_data["lifePointReduce"] = tmp_data["lifePointReduce"]["m_value"]
            base_data["rangeRadius"] = tmp_data["rangeRadius"]["m_value"]
            base_data["talent"] = tmp_data["talentBlackboard"]
            base_data["skills"] = tmp_data["skills"]
            base_data["spData"] = tmp_data["spData"]
            base_data["moveSpd"] = tmp_data["attributes"]["moveSpeed"]["m_value"]
            base_data["atkTime"] = tmp_data["attributes"]["baseAttackTime"]["m_value"]
            base_data["hpRec"] = tmp_data["attributes"]["hpRecoveryPerSec"]["m_value"]
            base_data["spRec"] = tmp_data["attributes"]["spRecoveryPerSec"]["m_value"]
            base_data["massLevel"] = tmp_data["attributes"]["massLevel"]["m_value"]
            # 免疫
            base_data["immune"] = [0, 0, 0]
            base_data["immune"][0] = tmp_data["attributes"]["stunImmune"]["m_value"]
            base_data["immune"][1] = tmp_data["attributes"]["silenceImmune"]["m_value"]
            base_data["immune"][2] = tmp_data["attributes"]["sleepImmune"]["m_value"]            
            # 提取数据（可变的）
            base_data["maxHp"] = []
            for i in range(level):
                if em["Value"][i]["enemyData"]["attributes"]["maxHp"]["m_defined"] == True:
                    base_data["maxHp"].append(em["Value"][i]["enemyData"]["attributes"]["maxHp"]["m_value"])
                else:
                    base_data["maxHp"].append(em["Value"][0]["enemyData"]["attributes"]["maxHp"]["m_value"])            
            base_data["atk"] = []
            for i in range(level):
                if em["Value"][i]["enemyData"]["attributes"]["atk"]["m_defined"] == True:
                    base_data["atk"].append(em["Value"][i]["enemyData"]["attributes"]["atk"]["m_value"])
                else:
                    base_data["atk"].append(em["Value"][0]["enemyData"]["attributes"]["atk"]["m_value"])
            base_data["def"] = []
            for i in range(level):
                if em["Value"][i]["enemyData"]["attributes"]["def"]["m_defined"] == True:
                    base_data["def"].append(em["Value"][i]["enemyData"]["attributes"]["def"]["m_value"])
                else:
                    base_data["def"].append(em["Value"][0]["enemyData"]["attributes"]["def"]["m_value"])
            base_data["magRes"] = []
            for i in range(level):
                if em["Value"][i]["enemyData"]["attributes"]["magicResistance"]["m_defined"] == True:
                    base_data["magRes"].append(em["Value"][i]["enemyData"]["attributes"]["magicResistance"]["m_value"])
                else:
                    base_data["magRes"].append(em["Value"][0]["enemyData"]["attributes"]["magicResistance"]["m_value"])
            # 将 base_data 存入 self.enemy_data
            self.enemy_data[tmp_key] = base_data
        
        # 存储数据到 enemydata.json
        # 生成文件，用 vscode 以 GB2312 打开，并以 UTF-8 重新编码保存
        filename = "enemydata.json"
        with open(filename, "w") as f:
            json.dump(self.enemy_data, f, ensure_ascii=False, sort_keys=True, indent=2)

#==============================================================================================#
#======================================= 用于干员数据的转换 ======================================#
class EmployeeDataSwitch(object):
    # 初始化参数
    def __init__(self):
        self.data_json = {}
        self.employee_list = {}
        self.employee_data = {}

    # 入口函数
    def letsEmployeeSwitch(self):
        self.getJsonData()
        self.getEmployeeList()
        self.getEmployeeData()
    
    # 获取原始的json文件: character_table.json
    def getJsonData(self):
        # 获取 character_table.json 干员属性表
        with open("character_table.json", encoding="utf-8") as f:
            self.data_json = json.load(f)

    # 生成干员列表 employeelist.json    
    def getEmployeeList(self):
        pass

    # 生成干员数据表 employeedata.json, 召唤物数据表 tokendata.json
    def getEmployeeData(self):
        for em in self.data_json:
            tmp_key = em
            tmp_data = self.data_json[em]
            base_data = {}
            if "char" in tmp_key:
                # 除去： canUseGen..., potentialItemId, nationId, groupId, teamId, tokenKey
                # itemDesc, itemObt..., isNotObt..., isSpChar, character..., 
                # 不变数据
                base_data["Key"] = tmp_key
                base_data["name"] = tmp_data["name"]
                base_data["description"] = tmp_data["description"]
                base_data["displayNum"] = tmp_data["displayNumber"]
                base_data["appellation"] = tmp_data["appellation"]
                base_data["position"] = tmp_data["position"]
                base_data["tagList"] = tmp_data["tagList"]
                base_data["itemUsage"] = tmp_data["itemUsage"]
                base_data["maxPotential"] = tmp_data["maxPotentialLevel"]
                base_data["rarity"] = tmp_data["rarity"]
                base_data["profession"] = tmp_data["profession"]
                base_data["trait"] = tmp_data["trait"]

                base_data["atkSpd"] = tmp_data["phases"][0]["attributesKeyFrames"][0]["data"]["attackSpeed"]
                base_data["hpRec"] = tmp_data["phases"][0]["attributesKeyFrames"][0]["data"]["hpRecoveryPerSec"]
                base_data["spRec"] = tmp_data["phases"][0]["attributesKeyFrames"][0]["data"]["spRecoveryPerSec"]
                base_data["atkTime"] = tmp_data["phases"][0]["attributesKeyFrames"][0]["data"]["baseAttackTime"]
                base_data["respawnTime"] = tmp_data["phases"][0]["attributesKeyFrames"][0]["data"]["respawnTime"]

                # 可变数据
                # 除去： character..., level, movespeed, maxDeployCount, tauntLevel, massLevel,
                # baseForceLevel, stunImmune, silenceImmune, sleepImmune, evolveCost
                base_data["range"] = []
                base_data["maxLevel"] = []
                base_data["maxHp"] = []
                base_data["atk"] = []
                base_data["def"] = []
                base_data["magRes"] = []
                base_data["cost"] = []
                base_data["blockCnt"] = []
                base_data["maxDeckStack"] = []
                for phase in tmp_data["phases"]:
                    base_data["range"].append(phase["rangeId"])
                    base_data["maxLevel"].append(phase["maxLevel"])
                    att_tmp = phase["attributesKeyFrames"]
                    base_data["maxHp"].append([att_tmp[0]["data"]["maxHp"], att_tmp[1]["data"]["maxHp"]])
                    base_data["atk"].append([att_tmp[0]["data"]["atk"], att_tmp[1]["data"]["atk"]])
                    base_data["def"].append([att_tmp[0]["data"]["def"], att_tmp[1]["data"]["def"]])
                    base_data["magRes"].append([att_tmp[0]["data"]["magicResistance"], att_tmp[1]["data"]["magicResistance"]])
                    base_data["cost"].append(att_tmp[0]["data"]["cost"])
                    base_data["blockCnt"].append(att_tmp[0]["data"]["blockCnt"])
                    base_data["maxDeckStack"].append(att_tmp[0]["data"]["maxDeckStackCnt"])
                print(base_data)
            elif "token" in tmp_key:
                pass
            break

if __name__ == "__main__": 
    # A = EnemyDataSwitch()
    # A.letsEnemySwitch()
    B = EmployeeDataSwitch()
    B.letsEmployeeSwitch()