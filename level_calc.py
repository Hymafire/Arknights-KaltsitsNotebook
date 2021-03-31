import json

# 用于计算干员当前等级的属性


class LevelCalculate(object):
    # 初始化参数
    def __init__(self):
        self.employee_param = {}
        self.employee_max = {}
        self.employee_min = {}
        self.favor = {}
        self.employee_max_level = 0
        self.employee_min_level = 0

    # 入口 main()
    def compute(self, name: str, elite: int, level: int, favor_level: int = 100, potential_rank: int = 0):
        self.name = name
        self.elite = elite
        self.level = level
        self.favor_level = favor_level
        self.potential_rank = potential_rank
        self.getParam()
        if self.judgeLegal():
            self.levelCalc()
            self.favorCalc()
            self.potentialCalc()
            self.talentCalc()
            return self.employee
        else:
            return "错误参数."

    # 计算相应等级数值
    def levelCalc(self):
        max_level_diff = self.employee_max_level - self.employee_min_level
        level_diff = self.level - self.employee_min_level
        self.employee = self.employee_min
        self.employee["maxHp"] += round(level_diff * (self.employee_max["maxHp"] -
                                                self.employee_min["maxHp"]) / max_level_diff)
        self.employee["atk"] += round(level_diff * (self.employee_max["atk"] -
                                              self.employee_min["atk"]) / max_level_diff)
        self.employee["def"] += round(level_diff * (self.employee_max["def"] -
                                              self.employee_min["def"]) / max_level_diff)

    # 计算信赖加成
    def favorCalc(self):
        self.employee["maxHp"] += round((min(self.favor_level,
                                       100) / 100) * self.favor["maxHp"])
        self.employee["atk"] += round((min(self.favor_level,
                                     100) / 100) * self.favor["atk"])
        self.employee["def"] += round((min(self.favor_level,
                                     100) / 100) * self.favor["def"])

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


if __name__ == "__main__":
    A = LevelCalculate()
    print(A.compute("伊芙利特", 2, 90))
