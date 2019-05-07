#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""

@created: 2019/5/6 17:12
@author: huangmin
@copyright: 2019 www.mindasoft.com Inc. All rights reserved.
"""
import tornado.web


class Do(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')
