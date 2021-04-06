from django.contrib import admin
from .models import EmployeeInfo
from .models import EmployeeData
from .models import EmployeeSkill
from .models import EmployeeTalent
from .models import EmployeePotential
from .models import EmployeeFavor
from .models import EnemyInfo
from .models import EnemyData
from .models import SkillsTable

# Register your models here.

@admin.register(EmployeeInfo)
class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'appellation', 'profession', 'rarity')

@admin.register(EmployeeData)
class EmployeeDataAdmin(admin.ModelAdmin):
    list_display = ('key',)

@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ('key',)

@admin.register(EmployeeTalent)
class EmployeeTalentAdmin(admin.ModelAdmin):
    list_display = ('key',)

@admin.register(EmployeePotential)
class EmployeePotentialAdmin(admin.ModelAdmin):
    list_display = ('key',)

@admin.register(EmployeeFavor)
class EmployeeFavorAdmin(admin.ModelAdmin):
    list_display = ('key',)

@admin.register(EnemyInfo)
class EnemyInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EnemyData)
class EnemyDataAdmin(admin.ModelAdmin):
    list_display = ('key',)

@admin.register(SkillsTable)
class SkillsTableAdmin(admin.ModelAdmin):
    list_display = ('key',)

