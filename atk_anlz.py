from level_calc import LevelCalculate

# 计算输出能力

class AttackAnalysis(object):
    # 初始化参数
    def __init__(self):
        self.em = {}
        self.pre_atk = 0

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

    # 秒伤图形化
    def preDamageGraph(self):
        pass


if __name__ == "__main__":
    A = AttackAnalysis()
    A.getParam("斯卡蒂", 2, 90)
    print(A.minDamage())
