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
        self.enemy_list = []            # 敌方列表 (kaltsit-web/enemy 树形控件:data参数)

    # 入口函数 
    def letsEnemySwitch(self):
        self.getJsonData()
        self.getEnemyData()
        self.getEnemyList()
        self.outputJson()

    #================================= json文件的处理 ===================================#
    def getJsonData(self):
        # 获取 enemy_database.json
        with open("enemy_database.json", encoding="utf-8") as f:
            self.data_json = json.load(f)        
        # 获取 enemy_handbook_table.json
        with open("enemy_handbook_table.json", encoding="utf-8") as f:
            self.handbook_json = json.load(f)

    def outputJson(self):
        # 生成文件，用 vscode 以 GB2312 打开，并以 UTF-8 重新编码保存
        # 敌人数据 enemydata.json
        filename = "enemydata.json"
        with open(filename, "w") as f:
            json.dump(self.enemy_data, f, ensure_ascii=False, sort_keys=True, indent=2)
        
        # 敌人列表 enemylist.json
        filename = "enemylist.json"
        with open(filename, "w") as f:
            json.dump(self.enemy_list, f, ensure_ascii=False, sort_keys=True, indent=2)
    
    #================================ 处理json文件中的数据 ================================#
    # 生成敌方列表 enemylist.json
    # enemyLevel: NORMAL, ELITE, BOSS
    def getEnemyList(self):
        # 分类生成子列表
        enemy_chi_list = [[], [], []]
        enemy_dict = {"NORMAL": 0, "ELITE": 1, "BOSS":2}
        for em in self.handbook_json:
            enemy_chi_dict = {}
            enemy_chi_dict["name"] = self.handbook_json[em]["name"]
            enemy_chi_list[enemy_dict[self.handbook_json[em]["enemyLevel"]]].append(enemy_chi_dict)
        # 敌人列表
        self.enemy_list.append({
            "name": "普通",
            "children": enemy_chi_list[0]
        })
        self.enemy_list.append({
            "name": "精英",
            "children": enemy_chi_list[1]
        })
        self.enemy_list.append({
            "name": "领袖",
            "children": enemy_chi_list[2]
        })
        print(self.enemy_list)
        
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
            base_data["atk"] = []
            base_data["def"] = []
            base_data["magRes"] = []
            for i in range(level):
                if em["Value"][i]["enemyData"]["attributes"]["maxHp"]["m_defined"] == True:
                    base_data["maxHp"].append(em["Value"][i]["enemyData"]["attributes"]["maxHp"]["m_value"])
                else:
                    base_data["maxHp"].append(em["Value"][0]["enemyData"]["attributes"]["maxHp"]["m_value"])            

                if em["Value"][i]["enemyData"]["attributes"]["atk"]["m_defined"] == True:
                    base_data["atk"].append(em["Value"][i]["enemyData"]["attributes"]["atk"]["m_value"])
                else:
                    base_data["atk"].append(em["Value"][0]["enemyData"]["attributes"]["atk"]["m_value"])

                if em["Value"][i]["enemyData"]["attributes"]["def"]["m_defined"] == True:
                    base_data["def"].append(em["Value"][i]["enemyData"]["attributes"]["def"]["m_value"])
                else:
                    base_data["def"].append(em["Value"][0]["enemyData"]["attributes"]["def"]["m_value"])

                if em["Value"][i]["enemyData"]["attributes"]["magicResistance"]["m_defined"] == True:
                    base_data["magRes"].append(em["Value"][i]["enemyData"]["attributes"]["magicResistance"]["m_value"])
                else:
                    base_data["magRes"].append(em["Value"][0]["enemyData"]["attributes"]["magicResistance"]["m_value"])
            # 将 base_data 存入 self.enemy_data
            self.enemy_data[tmp_key] = base_data     

#==============================================================================================#
#======================================= 用于干员数据的转换 ======================================#
class EmployeeDataSwitch(object):
    # 初始化参数
    def __init__(self):
        self.data_json = {}
        self.employee_list = []
        self.employee_data = {}
        self.token_data = {}

    # 入口函数
    def letsEmployeeSwitch(self):
        self.getJsonData()
        self.getEmployeeData()
        self.getEmployeeList()
        # self.outputJson()

    #=================================== json文件的处理 ============================================#
    # 获取原始的json文件: character_table.json
    def getJsonData(self):
        # 获取 character_table.json 干员属性表
        with open("character_table.json", encoding="utf-8") as f:
            self.data_json = json.load(f)

    # 输出json文件
    def outputJson(self):
        # 生成文件，用 vscode 以 GB2312 打开，并以 UTF-8 重新编码保存
        # 干员数据表 employeedata.json
        filename = "employeedata.json"
        with open(filename, "w") as f:
            json.dump(self.employee_data, f, ensure_ascii=False, sort_keys=True, indent=2)

        # 召唤物数据表 tokendata.json

        # 干员名单 employeelist.json
        filename = "employeelist.json"
        with open(filename, "w") as f:
            json.dump(self.employee_list, f, ensure_ascii=False, sort_keys=True, indent=2)

    #=================================== 处理json文件中的数据 ========================================#
    # 生成干员列表 employeelist.json
    def getEmployeeList(self):        
        # 获得子列表
        # 格式化 "干员"=>"{name:"干员"}"
        em_chi_list = [[], [], [], [], [], [], []]
        # 职业匹配字典
        prof_dic = {"PIONEER":0, "SNIPER":1, "MEDIC":2, "CASTER":3, "WARRIOR":4, "TANK":5, "SUPPORT":6, "SPECIAL":7}
        for em in self.data_json:
            # 判断干员/召唤物
            if "char" in em:
                em_chi_list[self.data_json[em]["rarity"]].append(em)
            elif "token" in em:
                em_chi_list[6].append({"name": self.data_json[em]["name"]})
        # 职业区分(召唤物不做区分)
        for i in range(len(em_chi_list) - 1):
            # 干员较少的不做区分
            if len(em_chi_list[i]) < 10:
                for j in range(len(em_chi_list[i])):
                    em_chi_list[i][j] = {"name": self.data_json[em_chi_list[i][j]]["name"]}
            else:
                em_prof_chi_list = [[], [], [], [], [], [], [], []]
                for em in em_chi_list[i]:
                    em_prof_chi_list[prof_dic[self.data_json[em]["profession"]]].append({"name": self.data_json[em]["name"]})
                # 替换未区分的列表    
                em_chi_list[i] = em_prof_chi_list
        # 干员列表
        # 职业匹配列表
        prof_list = ["PIONEER", "SNIPER", "MEDIC", "CASTER", "WARRIOR", "TANK", "SUPPORT", "SPECIAL"]
        # 匹配星级 (不包括 1,2星干员, 召唤物)
        for i in range(5, 1, -1):
            # 匹配职业
            tmp_chi_list = []
            for j in range(len(em_chi_list[i])):
                # 只保留有干员职业
                if em_chi_list[i][j] != []:
                    tmp_chi_dict = {}
                    tmp_chi_dict["name"] = prof_list[j]
                    tmp_chi_dict["children"] = em_chi_list[i][j]
                    tmp_chi_list.append(tmp_chi_dict)
            tmp_fa_dict = {}
            tmp_fa_dict["name"] = "{}".format("★" * (i+1))
            tmp_fa_dict["children"] = tmp_chi_list
            self.employee_list.append(tmp_fa_dict)
        # 匹配星级 (1,2星)
        for i in [1, 0]:
            tmp_fa_dict = {}
            tmp_fa_dict["name"] = "{}".format("★" *(i+1))
            tmp_fa_dict["children"] = em_chi_list[i]
            self.employee_list.append(tmp_fa_dict)
        # 匹配召唤物
        tmp_fa_dict = {}
        tmp_fa_dict["name"] = "召唤物"
        tmp_fa_dict["children"] = em_chi_list[6]
        self.employee_list.append(tmp_fa_dict)

    # 生成干员数据表 employeedata.json, 召唤物数据表 tokendata.json
    def getEmployeeData(self):
        for em in self.data_json:
            tmp_key = em
            tmp_data = self.data_json[em]
            base_data = {}    # 基数据
            # 干员数据
            if "char" in tmp_key:
                # 基础数据 ======================================================#
                # 除去： canUseGen..., potentialItemId, nationId, groupId, teamId, tokenKey
                # itemDesc, itemObt..., isNotObt..., isSpChar, character..., allSkillLvlup
                base_data["Key"] = tmp_key
                base_data["name"] = tmp_data["name"]
                base_data["description"] = tmp_data["description"]
                base_data["displayNum"] = tmp_data["displayNumber"]
                base_data["tokenKey"] = tmp_data["tokenKey"]
                base_data["appellation"] = tmp_data["appellation"]
                base_data["position"] = tmp_data["position"]
                base_data["tagList"] = tmp_data["tagList"]
                base_data["itemUsage"] = tmp_data["itemUsage"]
                base_data["maxPotential"] = tmp_data["maxPotentialLevel"]
                base_data["rarity"] = tmp_data["rarity"]
                base_data["profession"] = tmp_data["profession"]
                base_data["trait"] = tmp_data["trait"]

                # phases 阶段数据 ================================================#
                # 除去： character..., level, movespeed, maxDeployCount, tauntLevel, massLevel,
                # baseForceLevel, stunImmune, silenceImmune, sleepImmune, evolveCost
                # 不变的
                phases_data = {}
                phases_tmp = tmp_data["phases"][0]["attributesKeyFrames"][0]["data"]
                phases_data["atkSpd"] = phases_tmp["attackSpeed"]
                phases_data["hpRec"] = phases_tmp["hpRecoveryPerSec"]
                phases_data["spRec"] = phases_tmp["spRecoveryPerSec"]
                phases_data["atkTime"] = phases_tmp["baseAttackTime"]
                phases_data["respawnTime"] = phases_tmp["respawnTime"]
                # 变化的
                phases_data["range"] = []
                phases_data["maxLevel"] = []
                phases_data["maxHp"] = []
                phases_data["atk"] = []
                phases_data["def"] = []
                phases_data["magRes"] = []
                phases_data["cost"] = []
                phases_data["blockCnt"] = []
                phases_data["maxDeckStack"] = []
                for phase in tmp_data["phases"]:
                    phases_data["range"].append(phase["rangeId"])
                    phases_data["maxLevel"].append(phase["maxLevel"])
                    att_tmp = phase["attributesKeyFrames"]
                    phases_data["maxHp"].append([att_tmp[0]["data"]["maxHp"], att_tmp[1]["data"]["maxHp"]])
                    phases_data["atk"].append([att_tmp[0]["data"]["atk"], att_tmp[1]["data"]["atk"]])
                    phases_data["def"].append([att_tmp[0]["data"]["def"], att_tmp[1]["data"]["def"]])
                    phases_data["magRes"].append(att_tmp[0]["data"]["magicResistance"])
                    phases_data["cost"].append(att_tmp[0]["data"]["cost"])
                    phases_data["blockCnt"].append(att_tmp[0]["data"]["blockCnt"])
                    phases_data["maxDeckStack"].append(att_tmp[0]["data"]["maxDeckStackCnt"])
                # 将 phases_data 存入 base_data
                base_data["phases"] = phases_data

                # skills 技能数据 ==============================================#
                # 只保留 skillId
                base_data["skills"] = []
                for skill in tmp_data["skills"]:
                    base_data["skills"].append(skill["skillId"])
                
                # talents 天赋数据 ==============================================#
                # 保留全部
                base_data["talents"] = []
                if tmp_data["talents"] == None:
                    pass
                else:
                    for talent in tmp_data["talents"]:
                        base_data["talents"].append(talent["candidates"])

                # potential 潜能数据 ============================================#
                # 对天赋加强的潜能在天赋中计算
                # 保留 type, description, attributeModifiers, value               
                base_data["potential"] = []
                # 潜能匹配字典
                pot_dic = {0:"maxHp", 1:"atk", 2:"def", 3:"magRes", 4:"cost", 7:"atkSpd", 21:"respawnTime"}
                for i in range(base_data["maxPotential"]):
                    pot_data = {}
                    pot_data["type"] = tmp_data["potentialRanks"][i]["type"]
                    pot_data["description"] = tmp_data["potentialRanks"][i]["description"]
                    if pot_data["type"] == 1:
                        # 天赋增强潜能 默认成 ( maxHp + 0 )
                        pot_data["attType"] = "maxHp" 
                        pot_data["value"] = 0
                    elif pot_data["type"] == 0:
                        # 0:最大生命(maxHp) 1:攻击力(atk) 2:防御力(def) 3:法抗(magRes) 4:部署费用(cost) 7:攻击速度(atkSpd) 21:在部署时间(respawnTime)
                        pot_tmp = tmp_data["potentialRanks"][i]["buff"]["attributes"]["attributeModifiers"][0]
                        pot_data["attType"] = pot_dic[pot_tmp["attributeType"]]
                        pot_data["value"] = pot_tmp["value"]
                    base_data["potential"].append(pot_data)
            
                # favor 信赖数据 ================================================#
                # 保留 maxHp, atk, def
                favor_data = {}
                fav_tmp = tmp_data["favorKeyFrames"][1]["data"]
                favor_data["maxHp"] = fav_tmp["maxHp"]
                favor_data["atk"] = fav_tmp["atk"]
                favor_data["def"] = fav_tmp["def"]
                base_data["favor"] = favor_data

                # 将 base_data 存入 self.employee_data
                self.employee_data[tmp_key] = base_data
                
            # 召唤物数据
            elif "token" in tmp_key:
                pass



if __name__ == "__main__": 
    A = EnemyDataSwitch()
    A.letsEnemySwitch()
    # B = EmployeeDataSwitch()
    # B.letsEmployeeSwitch()