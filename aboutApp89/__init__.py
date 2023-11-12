# __init__.py文件竟然可以修改app名字
from os import path
from django.apps import AppConfig  # 修改名字主要用到的是django.apps模块中的AppConfig方法

VERBOSE_APP_NAME = '公司简介'  # VERBOSE_APP_NAME通过修改VERBOSE_APP_NAME字段为应用添加别名


def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME  # 设置别名


default_app_config = get_current_app_name(
    __file__) + '.__init__.AppVerboseNameConfig'
