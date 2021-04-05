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

class EmployeeSkillData(models.Model):
    pass



class EnemyData(models.Model):
    # 敌人基本信息
    Key = models.CharField("键值", max_length=30, primary_key=True, unique=True)
    name = models.CharField("名字", max_length=30)
    description = models.TextField("描述", null=True)
    life_point_reduce = models.IntegerField("", null=True)
    range_radius = models.FloatField("", null=True)
    talent_black_board = models.CharField("", null=True, max_length=20)
    skills = models.CharField("", null=True, max_length=30)
    spdata = models.CharField("", null=True, max_length=30) 
    # 敌人数据信息
    max_hp = models.IntegerField("最大血量", null=True)
    atk = models.IntegerField("攻击", null=True)
    defd = models.IntegerField("防御", null=True)
    mag_res = models.IntegerField("法抗", null=True)
    cost = models.IntegerField("部署费用", null=True)
    block_cnt = models.IntegerField("", null=True)
    move_speed = models.FloatField("移动速度", null=True)
    attack_speed = models.FloatField("攻速", null=True)
    base_atk_time = models.FloatField("攻击间隔", null=True)
    respqwn_time = models.IntegerField("", null=True)
    hp_rec_pre_sec = models.FloatField("", null=True)
    sp_rec_pre_sec = models.FloatField("", null=True)
    max_deploy_cnt = models.IntegerField("", null=True)
    mass_level = models.IntegerField("重量", null=True)
    base_force_level = models.IntegerField("嘲讽等级", null=True)
    stun_immune = models.BooleanField("")
    silence_immune = models.BooleanField("")
    sleep_immune = models.BooleanField("")
