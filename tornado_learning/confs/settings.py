# -*- coding: utf-8 -*-
"""
配置文件加载
@created: 2019-05-06 14:40
@author: huangmin
@copyright: 2019 www.mindasoft.com Inc. All rights reserved.
"""

import tornado.options as options
options.define('port', default=8002, type=int, help='Run on the given port')
options.define('config', default='dev', type=str, help='dev|prod|test')
options.parse_command_line()
if options.options.config == 'prod':
    from confs.settings_prod import *
elif options.options.config == 'test':
    from confs.settings_test import *
else:
    from confs.settings_dev import *
