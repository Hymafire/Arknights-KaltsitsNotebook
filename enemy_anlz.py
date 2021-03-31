import json

# 敌人危险程度分析

class EnemyAnalysis(object):

    def __init__(self):
        self.enemy_param = {}

    # 读参
    def getParam(self, name: str, level: int = 0):
        with open("enemy_table.json", encoding="utf-8") as f:
            json_file = json.load(f)
            for i in range(len(json_file)):
                enemy_file = json_file[i]
                if enemy_file["Value"][level]["enemyData"]["name"]["m_value"] == name:
                    self.enemy_param = enemy_file
        return self.enemy_param

    def attackCalc(self):
        pass


if __name__ == "__main__":
    A = EnemyAnalysis()
    print(A.getParam("源石虫"))
