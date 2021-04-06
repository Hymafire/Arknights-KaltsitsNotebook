from django.db import models

# Create your models here.


# 基础信息
class EmployeeInfo(models.Model):
 
    key = models.CharField("主键", max_length=30, primary_key=True, unique=True)
    name = models.CharField("名字", max_length=20)
    appellation = models.CharField("称号", max_length=20)
    description = models.TextField("描述", max_length=100)
    position = models.CharField("部署位", choices=(('MELEE', '近战位'), ('RANGED', '远程位')), max_length=10)
    max_potential_level = models.IntegerField("最大潜能")
    rarity = models.IntegerField("稀有度")
    profession = models.CharField("职业", max_length=10)
    trait = models.CharField("特性", null=True, max_length=10)  # 以后要改

    # 相关
    info_data = models.ForeignKey(to="EmployeeData", on_delete=models.CASCADE)
    info_skill = models.OneToOneField(to="EmployeeSkill", on_delete=models.CASCADE)
    info_talent = models.ForeignKey(to="EmployeeTalent", on_delete=models.CASCADE)
    info_potential = models.OneToOneField(to="EmployeePotential", on_delete=models.CASCADE)
    info_favor = models.OneToOneField(to="EmployeeFavor", on_delete=models.CASCADE)
    
# 阶段信息    
class EmployeeData(models.Model):    

    key= models.CharField("键", max_length=30, primary_key=True)
    phases = models.IntegerField("阶段",help_text="精0:(0,1),精1:(2,3),精2:(4,5)")
    range_id = models.CharField("攻击范围", max_length=10)
    max_level = models.IntegerField("最大等级")

    max_hp = models.IntegerField("最大血量")
    atk = models.IntegerField("攻击")
    defd = models.IntegerField("防御")
    mag_res = models.IntegerField("法抗")
    cost = models.IntegerField("部署费用")
    block_cnt = models.IntegerField("阻挡数")
    move_speed = models.FloatField("移动速度")
    attack_speed = models.FloatField("攻速")
    base_atk_time = models.FloatField("攻击间隔")
    respqwn_time = models.IntegerField("再部署时间")
    hp_rec_pre_sec = models.FloatField("生命恢复/秒")
    sp_rec_pre_sec = models.FloatField("技能回复/秒")
    max_deploy_cnt = models.IntegerField("最大召唤物数")
    mass_level = models.IntegerField("重量")
    base_force_level = models.IntegerField("嘲讽等级")
    stun_immune = models.BooleanField("眩晕免疫")
    silence_immune = models.BooleanField("沉默免疫")
    sleep_immune = models.BooleanField("睡眠免疫")

# 技能表    
class EmployeeSkill(models.Model):

    key = models.CharField("键", max_length=30, primary_key=True, unique=True)
    skill_1 = models.CharField("一技能", max_length=30, null=True)
    skill_2 = models.CharField("二技能", max_length=30, null=True)
    skill_3 = models.CharField("三技能", max_length=30, null=True)

    # 相关
    skill_1_skills = models.ForeignKey(to="SkillsTable", to_field="key", related_name="skill_1", null=True, on_delete=models.SET_NULL)
    skill_2_skills = models.ForeignKey(to="SkillsTable", to_field="key", related_name="skill_2", null=True, on_delete=models.SET_NULL)
    skill_3_skills = models.ForeignKey(to="SkillsTable", to_field="key", related_name="skill_3", null=True, on_delete=models.SET_NULL)

# 技能信息
class SkillsTable(models.Model):

    key = models.CharField("键", max_length=30, primary_key=True, unique=True)

# 天赋信息    
class EmployeeTalent(models.Model):

    key = models.CharField("键", max_length=30, primary_key=True, unique=True)

# 潜能信息    
class EmployeePotential(models.Model):

    key = models.CharField("键", max_length=30, primary_key=True, unique=True)

# 信赖信息    
class EmployeeFavor(models.Model):

    key = models.CharField("键", max_length=30, primary_key=True, unique=True)


# 敌人基本信息
class EnemyInfo(models.Model):
    
    key = models.CharField("主键", max_length=30, primary_key=True, unique=True)
    name = models.CharField("名字", max_length=30)
    description = models.TextField("描述", null=True)
    life_point_reduce = models.IntegerField("", null=True)
    range_radius = models.FloatField("", null=True)
    talent_black_board = models.CharField("", null=True, max_length=20)
    skills = models.CharField("技能", null=True, max_length=30)
    spdata = models.CharField("技力条", null=True, max_length=30) 
    
    # 相关
    info_data = models.ForeignKey(to="EnemyData", on_delete=models.CASCADE)


# 敌人数据信息
class EnemyData(models.Model):
    
    key = models.CharField("键", max_length=30, primary_key=True)
    level = models.IntegerField("等级")
    max_hp = models.IntegerField("最大血量", null=True)
    atk = models.IntegerField("攻击", null=True)
    defd = models.IntegerField("防御", null=True)
    mag_res = models.IntegerField("法抗", null=True)
    cost = models.IntegerField("部署费用", null=True)
    block_cnt = models.IntegerField("阻挡数", null=True)
    move_speed = models.FloatField("移动速度", null=True)
    attack_speed = models.FloatField("攻速", null=True)
    base_atk_time = models.FloatField("攻击间隔", null=True)
    respqwn_time = models.IntegerField("再部署时间", null=True)
    hp_rec_pre_sec = models.FloatField("生命恢复/秒", null=True)
    sp_rec_pre_sec = models.FloatField("技能回复/秒", null=True)
    max_deploy_cnt = models.IntegerField("最大召唤物数", null=True)
    mass_level = models.IntegerField("重量", null=True)
    base_force_level = models.IntegerField("嘲讽等级", null=True)
    stun_immune = models.BooleanField("眩晕免疫")
    silence_immune = models.BooleanField("沉默免疫")
    sleep_immune = models.BooleanField("睡眠免疫")
