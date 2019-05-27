from django.contrib import admin
from .models import InformationEmployee, Position
# Register your models here.


@ admin.register(InformationEmployee)
class InformationEmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'employment_day','salary','chief')


@ admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)