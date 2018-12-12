#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xadmin
from xadmin import views


class GlobalSetting(object):
    # 设置后台顶部标题   
    site_title = '我是后台管理'
    # 设置后台底部标题   
    site_footer = '我是底部信息'
    # 设置菜单可以折叠
    menu_style = 'accordion'


class BaseSetting(object):
    # 启用主题管理器   
    enable_themes = True
    # 使用主题   
    use_bootswatch = True


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
