import json

# 用于计算干员当前等级的属性

class level_calculate(object):
    # 初始化参数
    def __init__(self):
        self.em = {}
        self.em_max = {}
        self.em_min = {}
        self.favor = {}
        self.em_max_level = 0
        self.em_min_level = 0

    # 入口 main()
    def compute(self, name, elite, level, favor_level=100, potential_rank=0):
        self.name = name
        self.elite = elite
        self.level = level
        self.favor_level = favor_level
        self.potential_rank = potential_rank
        self.get_param()
        if self.judge():
            self.level_calculate()
            self.favor_calculate()
            self.potential_calculate()
            self.talent_calculate()
            return self.em
        else:
            return "错误参数."

    # 计算相应等级数值
    def level_calculate(self):
        max_level_diff = self.em_max_level - self.em_min_level
        level_diff = self.level - self.em_min_level
        self.em = self.em_min
        self.em["maxHp"] += round(level_diff * (self.em_max["maxHp"] -
                                                self.em_min["maxHp"]) / max_level_diff)
        self.em["atk"] += round(level_diff * (self.em_max["atk"] -
                                              self.em_min["atk"]) / max_level_diff)
        self.em["def"] += round(level_diff * (self.em_max["def"] -
                                              self.em_min["def"]) / max_level_diff)

    # 计算信赖加成
    def favor_calculate(self):
        self.em["maxHp"] += round((min(self.favor_level,
                                       100) / 100) * self.favor["maxHp"])
        self.em["atk"] += round((min(self.favor_level,
                                     100) / 100) * self.favor["atk"])
        self.em["def"] += round((min(self.favor_level,
                                     100) / 100) * self.favor["def"])

    # 计算潜能加成
    def potential_calculate(self):
        pass

    # 计算天赋加成
    def talent_calculate(self):
        pass

    # 读参
    def get_param(self):
        with open("employee_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
        for em in json_file:
            em_file = json_file[em]
            if em_file["name"] == self.name:
                rarity = em_file["rarity"]
                if rarity == 0 or rarity == 1:
                    if self.elite != 0:
                        return False
                elif rarity == 2:
                    if self.elite < 0 and self.elite > 1:
                        return False
                else:
                    if self.elite < 0 or self.elite > 2:
                        return False
                self.em_min_level = em_file["phases"][self.elite]["attributesKeyFrames"][0]["level"]
                self.em_min = em_file["phases"][self.elite]["attributesKeyFrames"][0]["data"]
                self.em_max_level = em_file["phases"][self.elite]["attributesKeyFrames"][1]["level"]
                self.em_max = em_file["phases"][self.elite]["attributesKeyFrames"][1]["data"]
                self.favor = em_file["favorKeyFrames"][1]["data"]
        return False

    # 读描述
    def get_description(self, name):
        with open("employee_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
        for em in json_file:
            em_file = json_file[em]
            if em_file["name"] == name:
                em_description = em_file["description"]
                return em_description
        return False

    # 判断输入参数是否合法
    def judge(self):
        if 1 <= self.level <= self.em_max_level and 0 <= self.favor_level <= 200:
            return True
        return False


if __name__ == "__main__":
    A = level_calculate()
    print(A.get_description("伊芙利特"))
