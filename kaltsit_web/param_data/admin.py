from django.contrib import admin
from .models import EmployeeData, EnemyData
# Register your models here.

@admin.register(EmployeeData)
class EmployeeDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'appellation', 'profession', 'rarity')
    
@admin.register(EnemyData)
class EnemyDataAdmin(admin.ModelAdmin):
    list_display = ('name',)