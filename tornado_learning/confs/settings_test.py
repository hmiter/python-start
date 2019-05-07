# -*- coding: utf-8 -*-
"""
测试配置文件
@created: 2019-05-06 14:40
@author: huangmin
@copyright: 2019 www.mindasoft.com Inc. All rights reserved.
"""

import sys
# python2.x 方式
# reload(sys)
# sys.setdefaultencoding("utf-8")  # 在Python2.x中由于str和byte之间没有明显区别，经常要依赖于defaultencoding来做转换

# python3.x 方式
import importlib
importlib.reload(sys)

from utils.db import MyConnection
from utils.log import SysLogger as Logger


# debug开关
DEBUG = False

'''
日志初使化
采用两种日志类型：stdout 和 syslog，线上系统采用syslog日志
stdout日志使用场景：研发环境的调试、NBE系统
'''
logger = Logger('tornado', Logger.INFO_LEVEL)

# mysql database configuration
db = MyConnection(
    host     = '192.168.1.55:3306',
    database = 'test',
    user     = '',
    password = '',
    logger   = logger
)

# 返回给ajax的数据
return_msg = dict(
    success = dict(
        err = 0,
        status = '00000',
        msg = '',
        seqid = ''
    ),
    error = dict(
        err = 1,
        status = -1,
        msg = u'系统错误',
        seqid = ''
    )
)

# 数据库ping的时间
db_ping_seconds = 1000

# 第三方帐号rtype类型， key必须是小写
rtypeConfig = dict(qq='100', tencent='110', weibo='200', wechat='300', xiaomi='400')

# 目录
# PROJECT_PATH = os.path.join(os.path.dirname(__file__), '..')
# tornado configuration
tornado_env = dict(
    #template_path       = os.path.join(PROJECT_PATH, "app", 'views'),
    template_path       = False,
    #static_path         = os.path.join(PROJECT_PATH, "static"),
    static_path         = False,
    xsrf_cookies        = False,
    cookie_secret       = "11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    autoescape          = None,
    debug               = DEBUG
)