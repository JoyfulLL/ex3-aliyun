from django.contrib import admin
from .models import MyNew
# Register your models here.


class MyNewAdmin(admin.ModelAdmin):
    # 定义style_field属性来绑定富文本字段
    style_field = {'description': 'ueditor'}


admin.site.register(MyNew, MyNewAdmin)
