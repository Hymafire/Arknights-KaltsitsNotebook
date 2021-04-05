from django.db import models

# Create your models here.

class EmployeeData(models.Model):

    # 基础信息
    key_name = models.CharField(verbose_name="关键名", max_length=30, primary_key=True, unique=True)
    name = models.CharField(verbose_name="名字", max_length=20)
    appellation = models.CharField(verbose_name="称号", max_length=20)
    description = models.TextField(verbose_name="描述", max_length=100)
    position = models.CharField(verbose_name="部署位", choices=(('MELEE', '近战位'), ('RANGED', '远程位')), max_length=10)
    max_potential_level = models.IntegerField(verbose_name="最大潜能")
    rarity = models.IntegerField(verbose_name="稀有度")
    profession = models.CharField(verbose_name="职业", max_length=10)
    trait = models.CharField(verbose_name="特性", null=True, max_length=10)  # 以后要改
    
    # 阶段信息
    


    # 技能信息



    # 天赋信息



    # 潜能信息



    # 信赖信息


