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
    
    # 入口,获得干员相关参数
    def get_param(self, employee_name, employee_elite, employee_level):
        self.employee = level_calculate().compute(employee_name, employee_elite, employee_level)
        self.atk = self.employee["atk"]
        self.attackSpeed = self.employee["attackSpeed"]
        self.baseAttackTime = self.employee["baseAttackTime"]

    # 计算秒伤
    def pre_damage(self, enemy_def = 0):        
        true_atk = max(self.atk * 0.05, self.atk - enemy_def)
        self.pre_atk = (true_atk / self.baseAttackTime) * (100 / self.attackSpeed)
        return "Dps:{:.1f}/s".format(self.pre_atk)
    
    # 保底伤害及保底线
    def min_damage(self, mod = 0):
        if mod == 0:    # min_pre_damage
            min_dam = (self.atk * 0.05 / self.baseAttackTime) * (100 / self.attackSpeed)
        else:           # min_hite_damage
            min_dam = self.atk * 0.05
        dam_line = self.atk * 0.95
        return "{:.1f},{:.1f}".format(min_dam, dam_line)
    

if __name__ == "__main__":
    A = attack_calculate()
    A.get_param("斯卡蒂", 2, 90)
    print(A.min_damage())
