# users/apps.py

from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'
    #app名字后台显示中文
    verbose_name = "用户管理"