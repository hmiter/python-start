#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 日志处理模块


import os
import sys
from utils import myjson
import logging
# import syslog
import traceback
import time


class BaseLogger(object):
    
    def __init__(self):
        pass

    def initialize(self):
        pass
    
    def debug(self, msg, ip='0.0.0.0'):
        """DEBUG"""
        self._log(self.DEBUG_LEVEL, msg, ip)

    def info(self, msg, ip='0.0.0.0'):
        """INFO"""
        self._log(self.INFO_LEVEL, msg, ip)

    def notice(self, msg, ip='0.0.0.0'):
        """NOTICE"""
        self._log(self.NOTICE_LEVEL, msg, ip)
    
    def warn(self, msg, ip='0.0.0.0'):
        """WARNING"""
        self._log(self.WARNING_LEVEL, msg, ip)
    
    def error(self, msg, ip='0.0.0.0'):
        """ERR"""
        self._log(self.ERR_LEVEL, msg, ip)
    
    def exception(self, ex):
        """ERR"""
        self.error(self.__exception_msg(ex))
    
    def __exception_msg(self, ex):
        t, v, tb = sys.exc_info()
        return '%s|%s|%s|%s' % (traceback.format_tb(tb), t, v, ex)

    def get_local_ip(self):
        ml = "ifconfig | grep 'inet addr:' | cut -d: -f2 | awk '{print  $1}' | awk '{print;exit}'"
        res = os.popen(ml).readlines()
        if res:
            return res[0].strip()
        else:
            return '127.0.0.1'


class StdLogger(BaseLogger):

    DEBUG_LEVEL     = 'DEBUG'
    INFO_LEVEL      = 'INFO'
    NOTICE_LEVLE    = 'NOTICE'
    WARNING_LEVEL   = 'WARNING'
    ERR_LEVEL       = 'ERR'

    def __init__(self, name, level=None):
        self.logdata = {}
        self.level = None
        self.server_name = name
        self.server_ip = self.get_local_ip()

    def _log(self, cate, msg, ip):
        try:
            msg = myjson.dumps(msg, ensure_ascii = False, indent = 2)
        except:
            msg = '%s' % msg
        time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        msg = '%s|%s|%s|%s|%s'%(self.server_ip, time_str, self.server_name, cate,  msg)
        print('\n',msg.replace("\\n",'\n\r'),'\n')


class SysLogger(BaseLogger):
    DEBUG_LEVEL = logging.DEBUG
    INFO_LEVEL = logging.INFO
    NOTICE_LEVLE = logging.NOTSET
    WARNING_LEVEL = logging.WARNING
    ERR_LEVEL = logging.ERROR

    def __init__(self, name, level):
        self.logdata = {}
        self.level = level
        self.server_name = name
        self.server_ip = self.get_local_ip()
        logging.basicConfig(level=self.level,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=self.server_name + '.log',
                            filemode='w')
    # % (levelno)s: 打印日志级别的数值
    # % (levelname)s: 打印日志级别名称
    # % (pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    # % (filename)s: 打印当前执行程序名
    # % (funcName)s: 打印日志的当前函数
    # % (lineno)d: 打印日志的当前行号
    # % (asctime)s: 打印日志的时间
    # % (thread)d: 打印线程ID
    # % (threadName)s: 打印线程名称
    # % (process)d: 打印进程ID
    # % (message)s: 打印日志信息

    def _log(self, cate, msg, ip):
        try:
            msg = myjson.dumps(msg)
        except:
            msg = '%s' % msg
        time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        msg = '%s|%s|%s|%d|%s' % (self.server_ip, time_str, self.server_name, cate,  msg)
        logging.log(cate,msg.encode('utf8'))



# class SysLogger(BaseLogger):
#     DEBUG_LEVEL = syslog.LOG_DEBUG
#     INFO_LEVEL = syslog.LOG_INFO
#     NOTICE_LEVLE = syslog.LOG_NOTICE
#     WARNING_LEVEL = syslog.LOG_WARNING
#     ERR_LEVEL = syslog.LOG_ERR
#
#     def __init__(self, name):
#         self.logdata = {}
#         self.server_name = name
#         self.server_ip = self.get_local_ip()
#         syslog.openlog('httpserver', syslog.LOG_PID, syslog.LOG_LOCAL1)
#
#     def _log(self, cate, msg, ip):
#         try:
#             msg = myjson.dumps(msg)
#         except:
#             msg = '%s' % msg
#         time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#         msg = '%s|%s|%s|%d|%s'%(self.server_ip, time_str, self.server_name, cate,  msg)
#         syslog.syslog(cate, msg.encode('utf8') if type(msg) == unicode else msg)
