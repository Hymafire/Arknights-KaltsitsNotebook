import json
import numpy as np
import matplotlib.pyplot as plt

from decimal import Decimal

# 敌人危险程度分析

class EnemyAnalysis(object):
    # 初始化
    def __init__(self):
        self.enemy_param = {}
        self.enemies_param = {}

    # 读参
    # level:敌人等级
    def getParam(self, name: str, level: int = 0):
        if name in self.enemies_param:
            self.enemy_param = self.enemies_param[name]
            return self.enemy_param
        with open("enemy_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
            for i in range(len(json_file)):
                enemy_file = json_file[i]["Value"][level]
                if enemy_file["enemyData"]["name"]["m_value"] == name:
                    self.enemy_param = enemy_file
                    break   
        return self.enemy_param

    # 登录敌人库
    def loadParam(self):
        name = self.enemy_param["enemyData"]["name"]["m_value"]
        if name not in self.enemies_param:
            self.enemies_param[name] = self.enemy_param[name]
        return self.enemies_param

    # 获取其中一条参数
    def getOneParam(self, param_mod: str):
        if self.enemy_param["enemyData"]["attributes"][param_mod]["m_defined"]:
            return self.enemy_param["enemyData"]["attributes"][param_mod]["m_value"]
        else:
            return "No Param"

    # 输出计算
    def preDamageCalc(self, employee_def: float = 0, employee_mag_res: float = 0):
        atk = self.enemy_param["enemyData"]["attributes"]["atk"]["m_value"]
        atk_spd = self.enemy_param["enemyData"]["attributes"]["attackSpeed"]["m_value"]
        base_atk_t = self.enemy_param["enemyData"]["attributes"]["baseAttackTime"]["m_value"]
        dam_mod = self.damageMod()
        if dam_mod == "Phy":
            true_dam = max(atk * 0.05, atk - employee_def)
        elif dam_mod == "Mag":
            true_dam = max(0.05, 1 - employee_mag_res / 100) * atk
        pre_dam = (true_dam / base_atk_t) * (100 / atk_spd)
        return pre_dam
        
    # 伤害类型
    def damageMod(self):
        dam_mod = "Phy"
        if "法术攻击" in self.enemy_param["enemyData"]["description"]["m_value"]:
            dam_mod = "Mag"
        return dam_mod
        
    def viablityCalc(self, enployee_atk: float = 700, employee_dam_mod: str = "Phy"):
        pass

    # 各参数在全体敌人中的排名
    def enemyInEnemies(self):
        rank_dic = {}
        for param_mod in self.enemy_param["enemyData"]["attributes"]:
            if self.enemy_param["enemyData"]["attributes"][param_mod]["m_defined"]:
                rank_dic[param_mod] = self.enemyRankInEnemies(param_mod)
        return rank_dic
    
    # 全体敌人参数平均值
    # level:（暂不设置！）
    def enemiesAverage(self, param_mod: str, level: int = 0):
        param_avg = 0
        with open("enemy_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
            for i in range(len(json_file)):
                enemy_file = json_file[i]["Value"][level]["enemyData"]
                param_avg += enemy_file["attributes"][param_mod]["m_value"]
            param_avg = param_avg / len(json_file)
        return param_avg

    # 所求敌人所选参数在所有敌人中的排名
    # return_mod: 0.数字排名 1.百分位排名
    def enemyRankInEnemies(self, param_mod: str, return_mod: int = 0):
        param_rank, enemy_num = 1, 0
        the_param = self.enemy_param["enemyData"]["attributes"][param_mod]["m_value"]
        with open("enemy_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
            enemy_num = len(json_file)
            for i in range(enemy_num):
                enemy_file = json_file[i]["Value"][0]["enemyData"]
                if the_param < enemy_file["attributes"][param_mod]["m_value"]:
                    param_rank += 1
        if return_mod == 0:
            return param_rank
        elif return_mod == 1:
            return (param_rank - 1) / enemy_num * 100 

    #======================================作图代码分割线======================================#

    def preDamageGraph(self):
        x = np.arange(self.enemy_param["enemyData"]["attributes"]["atk"]["m_value"] * 1.1)
        y = list()
        for step_def in x:
            y.append(self.preDamageCalc(step_def))
        plt.title("preDamage")
        plt.xlabel("Def")
        plt.ylabel("preDam")
        plt.plot(x,y)
        plt.show()

    def hitDamageGraph(self):
        x = np.arange(0.1, 15, 0.1)
        y = list()
        cnt = 0
        atk = self.enemy_param["enemyData"]["attributes"]["atk"]["m_value"]
        base_atk_t = self.enemy_param["enemyData"]["attributes"]["baseAttackTime"]["m_value"]
        atk_spd = self.enemy_param["enemyData"]["attributes"]["attackSpeed"]["m_value"]
        atk_time = base_atk_t * 100 / atk_spd
        for step_time in x:
            if int(step_time * 10) % int(atk_time * 10) == 0:
                cnt += atk
            y.append(cnt)
        plt.title("hitDamage")
        plt.xlabel("Time")
        plt.ylabel("hitDam")
        plt.plot(x,y)
        plt.show()

if __name__ == "__main__":
    A = EnemyAnalysis()
    A.getParam("源石虫")
    #print(A.enemyInEnemies())
    #print(A.enemiesAverage("atk"))
    #print(A.preDamageCalc())
    #print(A.getOneParam("atk"))
    A.hitDamageGraph()