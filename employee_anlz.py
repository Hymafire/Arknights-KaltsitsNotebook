import json

# 用于计算干员当前等级的属性

class LevelCalculate(object):
    # 初始化参数
    def __init__(self):
        self.employee_param = {}
        self.employee_max = {}
        self.employee_min = {}
        self.favor = {}
        self.potential = {}
        self.talent = {}
        self.employee_max_level = 0

    # 入口 main()
    def compute(self, name: str, elite: int, level: int, favor_level: int = 100, potential_rank: int = 0):
        self.getParam(name, elite)
        if self.judgeLegal():
            self.levelCalc(level)
            self.favorCalc(favor_level)
            self.potentialCalc(potential_rank)
            self.talentCalc(elite)
            return self.employee
        else:
            return "错误参数."

    # 计算相应等级数值
    # 其他属性暂不随等级变化而变化
    def levelCalc(self, level: int):
        level_diff = self.employee_max_level - 1
        self.employee = self.employee_min
        self.employee["maxHp"] += round((level - 1) * (self.employee_max["maxHp"] -
                                                self.employee_min["maxHp"]) / level_diff)
        self.employee["atk"] += round((level - 1) * (self.employee_max["atk"] -
                                              self.employee_min["atk"]) / level_diff)
        self.employee["def"] += round((level - 1) * (self.employee_max["def"] -
                                              self.employee_min["def"]) / level_diff)

    # 计算信赖加成
    # 信赖暂只加成"maxHp""atk""def"三个属性
    def favorCalc(self, favor_level: int):
        self.employee["maxHp"] += round(min(favor_level / 100, 1) * self.favor["maxHp"])                                   
        self.employee["atk"] += round(min(favor_level / 100, 1) * self.favor["atk"])                                
        self.employee["def"] += round(min(favor_level / 100, 1) * self.favor["def"])                                  

    # 计算潜能加成
    def potentialCalc(self):
        pass

    # 计算天赋加成
    def talentCalc(self):
        pass

    # 读参
    def getParam(self):
        with open("employee_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
        for employee in json_file:
            employee_file = json_file[employee]
            if employee_file["name"] == self.name:
                rarity = employee_file["rarity"]
                if rarity == 0 or rarity == 1:
                    if self.elite != 0:
                        return False
                elif rarity == 2:
                    if self.elite < 0 and self.elite > 1:
                        return False
                else:
                    if self.elite < 0 or self.elite > 2:
                        return False
                self.employee_min_level = employee_file["phases"][self.elite]["attributesKeyFrames"][0]["level"]
                self.employee_min = employee_file["phases"][self.elite]["attributesKeyFrames"][0]["data"]
                self.employee_max_level = employee_file["phases"][self.elite]["attributesKeyFrames"][1]["level"]
                self.employee_max = employee_file["phases"][self.elite]["attributesKeyFrames"][1]["data"]
                self.favor = employee_file["favorKeyFrames"][1]["data"]
                self.potential = employee_file["potentialRanks"]
                self.talent = employee_file["talents"]
        return False

    # 读描述
    def getDescription(self, name: str):
        with open("employee_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
        for employee in json_file:
            employee_file = json_file[employee]
            if employee_file["name"] == name:
                employee_description = employee_file["description"]
                return employee_description
        return False

    # 判断输入参数是否合法
    def judgeLegal(self):
        if 1 <= self.level <= self.employee_max_level and 0 <= self.favor_level <= 200:
            return True
        return False

#==========================================分割线==========================================#

class EmployeeAnalysis(object):
    # 初始化参数
    def __init__(self):
        self.em = {}

    # 获得干员相关参数
    def getParam(self, name: str, elite: str, level: str):
        self.name = name
        self.em = LevelCalculate().compute(name, elite, level)
        self.atk = self.em["atk"]
        self.atk_spd = self.em["attackSpeed"]
        self.base_atk_t = self.em["baseAttackTime"]

    # 计算秒伤
    def preDamage(self, enemy_def: int = 0, enemy_magicResistance: int = 0):
        dam_mod = self.damageMod(self.name)
        if dam_mod == "Mag":
            true_atk = max(0.05, 1 - enemy_magicResistance / 100) * self.atk
        elif dam_mod == "Phy":
            true_atk = max(self.atk * 0.05, self.atk - enemy_def)
        elif dam_mod == "Tru":
            true_atk = self.atk
        self.pre_atk = (true_atk / self.base_atk_t) * (100 / self.atk_spd)
        return self.pre_atk

    # 保底伤害及保底线
    def minDamage(self, mod: int = 0):
        if mod == 0:    # min_pre_damage
            min_dam = (self.atk * 0.05 / self.base_atk_t) * (100 / self.atk_spd)
        else:           # min_hite_damage
            min_dam = self.atk * 0.05
        dam_line = self.atk * 0.95
        ret = [min_dam, dam_line]
        return ret

    # 判断伤害模式
    def damageMod(self, name: str):
        description = LevelCalculate().getDescription(name)
        dam_mod = "Phy"
        if "法术伤害" in description:
            dam_mod = "Mag"
        elif "真实伤害" in description:
            dam_mod = "Tru"
        return dam_mod

    # 获得干员相关参数
    def get_param(self, name, elite, level):
        self.em = LevelCalculate().compute(name, elite, level)
        self.maxHp = self.em["maxHp"]
        self.def_ = self.em["def"]
        self.magicResistance = self.em["magicResistance"]
        self.hpRecoveryPerSec = self.em["hpRecoveryPerSec"]

    # 驻留时间
    def viability_compute(self, en_atk = 100, en_atkSpeed = 1.00, en_dam_mod = "Phy"):
        if en_dam_mod == "Phy":
            en_dam = max(en_atk - self.def_, en_atk * 0.05)
        elif en_dam_mod == "Mag":
            en_dam = min(0.05, 1 - self.magicResistance / 100) * en_atk
        now_Hp = self.maxHp
        stay_time = 0
        while now_Hp > 0:
            now_Hp -= en_dam
            stay_time += en_atkSpeed
        return stay_time

    # 秒伤图形化
    def preDamageGraph(self):
        pass


if __name__ == "__main__":
    A = LevelCalculate()
    print(A.compute("伊芙利特", 2, 90))
