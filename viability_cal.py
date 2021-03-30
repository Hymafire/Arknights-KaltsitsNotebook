from level_cal import level_calculate

# 计算生存能力

class viability_calculate(object):

    def __init__(self):
        pass

    # 获得干员相关参数
    def get_param(self, name, elite, level):
        self.em = level_calculate().compute(name, elite, level)
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


if __name__ == "__main__":
    A = viability_calculate()
    A.get_param("斯卡蒂", 2, 90)
    print(A.viability_compute(en_atk = 500))