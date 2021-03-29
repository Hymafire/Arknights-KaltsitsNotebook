from level_cal import level_calculate
import json

# 计算输出能力
class attack_calculate:
    # 初始化参数
    def __init__(self):
        self.em = {}
        self.atk = 0
        self.attackSpeed = 100.0
        self.baseAttackTime = 1.00
        self.pre_atk = 0
    
    # 入口,获得干员相关参数
    def get_param(self, name, elite, level):
        self.em = level_calculate().compute(name, elite, level)
        self.atk = self.em["atk"]
        self.attackSpeed = self.em["attackSpeed"]
        self.baseAttackTime = self.em["baseAttackTime"]

    # 计算秒伤
    def pre_damage(self, name):
        dam_mod = self.damage_mod(name)
        if dam_mod == "法术伤害":
            self.pre_damage_mag(enemy_magicResistance = 0)
        elif dam_mod == "真实伤害":
            self.pre_damage_tru()
        else:
            self.pre_damage_phy(enemy_def = 0)

    # 计算物理秒伤
    def pre_damage_phy(self, enemy_def):      
        true_atk = max(self.atk * 0.05, self.atk - enemy_def)
        self.pre_atk = (true_atk / self.baseAttackTime) * (100 / self.attackSpeed)
        return "Dps:{:.1f}/s".format(self.pre_atk)
    
    # 计算法术秒伤
    def pre_damage_mag(self, enemy_magicResistance):
        true_atk = max(0.05, 1 - enemy_magicResistance / 100) * self.atk
        self.pre_atk = (true_atk / self.baseAttackTime) * (100 / self.attackSpeed)
        return "Dps:{:.1f}/s".format(self.pre_atk)

    # 计算真实伤害
    def pre_damage_tru(self):
        self.pre_atk = (self.atk / self.baseAttackTime) * (100 / self.attackSpeed)
        return "Dps:{:.1f}/s".format(self.pre_atk)

    # 保底伤害及保底线
    def min_damage(self, mod = 0):
        if mod == 0:    # min_pre_damage
            min_dam = (self.atk * 0.05 / self.baseAttackTime) * (100 / self.attackSpeed)
        else:           # min_hite_damage
            min_dam = self.atk * 0.05
        dam_line = self.atk * 0.95
        return "{:.1f},{:.1f}".format(min_dam, dam_line)

    # 判断伤害模式
    def damage_mod(self, name):
        description = level_calculate().get_description(name)
        if "法术伤害" in description:
            dam_mod = "Mag"
        elif "真实伤害" in description:
            dam_mod = "Tru"
        return dam_mod

if __name__ == "__main__":
    A = attack_calculate()
    A.get_param("斯卡蒂", 2, 90)
    print(A.min_damage())
