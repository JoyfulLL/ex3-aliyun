from django.contrib import admin

# Register your models here.
from .models import Award


class AwardAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo']


admin.site.register(Award, AwardAdmin)

# 修改管理系统名称
admin.site.site_header = 'LJF的Django后台管理'
admin.site.site_title = 'LJF登录'
