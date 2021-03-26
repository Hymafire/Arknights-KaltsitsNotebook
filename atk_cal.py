from level_cal import level_calculate

# 计算输出能力
class attack_calculate:
    # 初始化参数
    def __init__(self):
        self.employee = {}
        self.atk = 0
        self.attackSpeed = 100.0
        self.baseAttackTime = 1.00
        self.pre_atk = 0
    
    # 入口 main()
    def atk_compute(self, employee_name, employee_elite, employee_level):
        self.name = employee_name
        self.elite = employee_elite
        self.level = employee_level
        self.employee = level_calculate().compute(self.name, self.elite, self.level)
        self.calculate()
        return self.pre_atk

    # 计算器
    def calculate(self):
        self.atk = self.employee["atk"]
        self.attackSpeed = self.employee["attackSpeed"]
        self.baseAttackTime = self.employee["baseAttackTime"]
        self.pre_atk = (self.atk / self.baseAttackTime) * (100 / self.attackSpeed)

if __name__ == "__main__":
    A = attack_calculate()
    print(A.atk_compute("斯卡蒂", 2, 90))