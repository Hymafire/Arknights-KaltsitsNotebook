import json

# 用于计算干员当前等级的属性
class level_calculate(object):
    #初始化参数
    def __init__(self):
        self.employee = {}
        self.employee_max = {}
        self.employee_min = {}
        self.employee_max_level = 0
        self.employee_min_level = 0
        self.name = ""
        self.elite = 0
        self.level = 0
    
    # 入口 main()
    def compute(self, employee_name, employee_elite, employee_level):
        self.name = employee_name
        self.elite = employee_elite
        self.level = employee_level
        self.get_param()
        return self.calculate()

    # 运算器
    def calculate(self):
        max_level_diff = self.employee_max_level - self.employee_min_level
        level_diff = self.level - self.employee_min_level
        self.employee = self.employee_min
        self.employee["maxHp"] += round(level_diff * (self.employee_max["maxHp"] - self.employee_min["maxHp"]) / max_level_diff)
        self.employee["atk"] += round(level_diff * (self.employee_max["atk"] - self.employee_min["atk"]) / max_level_diff)
        self.employee["def"] += round(level_diff * (self.employee_max["def"] - self.employee_min["def"]) / max_level_diff)
        return self.employee

    # 读参
    def get_param(self):
        with open("employee_table.json", encoding = "utf-8") as f:
            json_file = json.load(f)
        for employee in json_file:
            employee_file = json_file[employee]
            if employee_file["name"] == self.name:
                self.employee_min_level = employee_file["phases"][self.elite]["attributesKeyFrames"][0]["level"]
                self.employee_min = employee_file["phases"][self.elite]["attributesKeyFrames"][0]["data"]
                self.employee_max_level = employee_file["phases"][self.elite]["attributesKeyFrames"][1]["level"]                
                self.employee_max = employee_file["phases"][self.elite]["attributesKeyFrames"][1]["data"]


if __name__ == "__main__":
    A = level_calculate()
    print(A.compute("斯卡蒂", 1, 80))