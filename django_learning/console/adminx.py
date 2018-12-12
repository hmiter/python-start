#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xadmin
from xadmin import views


class GlobalSetting(object):
    # 设置后台顶部标题   
    site_title = '管理控制台'
    # 设置后台底部标题   
    site_footer = '2018 敏达软件 '
    # 设置菜单可以折叠
    menu_style = 'accordion'


class BaseSetting(object):
    # 启用主题管理器   
    enable_themes = True
    # 使用主题   
    use_bootswatch = True


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
