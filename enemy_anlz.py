import json
import numpy as np
import matplotlib.pyplot as plt

# 敌人危险程度分析

class EnemyAnalysis(object):
    # 初始化
    def __init__(self):
        self.enemy_param = {}

    # 读参
    # level:敌人等级
    def getParam(self, name: str, level: int = 0):
        self.name = name
        self.level = level
        with open("enemy_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
            for i in range(len(json_file)):
                enemy_file = json_file[i]["Value"][level]
                if enemy_file["enemyData"]["name"]["m_value"] == name:
                    self.enemy_param = enemy_file
                    break
        return self.enemy_param

    def attackCalc(self):
        pass

    def enemyInEnemies(self, param_mod: str):
        pass
    
    # 全体敌人参数平均值
    # level:（暂不设置！）
    def enemiesAverage(self, param_mod: str, level: int = 0):
        param_avg = 0
        with open("enemy_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
            for i in range(len(json_file)):
                enemy_file = json_file[i]["Value"][level]
                param_avg += enemy_file["enemyData"]["attributes"][param_mod]["m_value"]
            param_avg = param_avg / len(json_file)
        return param_avg

    # 所求敌人所选参数在所有敌人中的排名
    def enemyRankInEnemies(self, param_mod: str):
        param_rank = 0
        the_param = self.enemy_param["enemyData"]["attributes"][param_mod]["m_value"]
        with open("enemy_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
            for i in range(len(json_file)):
                enemy_file = json_file[i]["Value"][self.level]
                if the_param < enemy_file["enemyData"]["attributes"][param_mod]["m_value"]:
                    param_rank += 1
        return param_rank

# 图形化表示    
class EnemyAnalysisGraph(object):




if __name__ == "__main__":
    A = EnemyAnalysis()
    #print(A.getParam("源石虫"))
    #print(A.enemiesAverage("atk"))
    A.getParam("爱国者")
    print(A.enemyRankInEnemies("atk"))