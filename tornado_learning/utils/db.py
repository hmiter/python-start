#coding: utf-8
from __future__ import with_statement
from contextlib import contextmanager
from libs.torndb import *
import time


class MyConnection(Connection):
    
    def __init__(self, host, database, user=None, password=None,
                 max_idle_time=7*3600, logger=None, connect_timeout=0,
                 time_zone="+0:00", charset = "utf8", sql_mode="TRADITIONAL"):
        super(MyConnection, self).__init__(host, database, user, password, max_idle_time)
        self.logger = logger
        
    def _execute(self, cursor, query, parameters, kwparameters):
        try:
            params_str = '|'.join(map(str, parameters))
            begin_time = time.time()
            #self.logger.debug('MySQL|BEGIN|%s|%s' % (query, params_str))
            relt = cursor.execute(query, kwparameters or parameters)
            #self.logger.debug('MySQL|END|%s|%s|%s' % (time.time() - begin_time, query, params_str))
            end_time = time.time() - begin_time
            mysql_str = {'%s|%s|%s' % (end_time, query, params_str)}
            if not self.logger.logdata.has_key('mysql'):
                self.logger.logdata.update({'mysql':mysql_str,'mysql_used_time':end_time})
            else:
                self.logger.logdata['mysql_used_time'] = self.logger.logdata['mysql_used_time']+end_time
                self.logger.logdata['mysql'].update(mysql_str)
            return relt
        except OperationalError as ex:
            print (cursor._last_executed)
            self.logger.exception(ex)
            self.close()
            raise
    
    @contextmanager
    def transaction(self):
        t = Transaction(self._db)
        try:
            yield None
        except:
            t.rollback()
            raise
        else:
            t.commit()

    def __del__(self):
        self.close()
       
    '''
    自己扩展的插入方法
    ''' 
    def insert_by_dict(self, tablename, rowdict, replace=False):
        cursor = self._cursor()
        cursor.execute("describe %s" % tablename)
        allowed_keys = set(row[0] for row in cursor.fetchall())
        keys = allowed_keys.intersection(rowdict)
    
        if len(rowdict) > len(keys):
            unknown_keys = set(rowdict) - allowed_keys
            logging.error("skipping keys: %s", ", ".join(unknown_keys))
    
        columns = ", ".join(keys)
        values_template = ", ".join(["%s"] * len(keys))
    
        if replace:
            sql = "REPLACE INTO %s (%s) VALUES (%s)" % (
                tablename, columns, values_template)
        else:
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (
                tablename, columns, values_template)

        values = tuple(rowdict[key] for key in keys)
        try:
            # cursor.execute(sql, values)
            self._execute(cursor, sql, values, None)
            return cursor.lastrowid
        finally:
            cursor.close()
           
    '''
    自己扩展的更新方法
    ''' 
    def update_by_dict(self, tablename, rowdict, whereDict = None):
        arr = []
        columnField = whereField = ''
        for key in rowdict:
            columnField += ',' + key + ' = %s'
            arr.append(rowdict[key])
        if columnField:
            columnField = columnField[1:]
                        
        if whereDict:
            for key in whereDict:
                 whereField += ',' + key + ' = %s'
                 arr.append(whereDict[key])
            if whereField:
                whereField = ' WHERE ' + whereField[1:]
        
        sql = "UPDATE %s SET %s %s" % (tablename, columnField, whereField)
        cursor = self._cursor()
        try:
            self._execute(cursor, sql, arr, None)
            return cursor.rowcount
        finally:
            cursor.close()
            
    def exeArr(self, sql, arr):
        cursor = self._cursor()
        try:
            self._execute(cursor, sql, arr, None)
            column_names = [d[0] for d in cursor.description]
            print([Row(itertools.izip(column_names, row)) for row in cursor])
        finally:
            cursor.close()


class Transaction(object):
    
    def __init__(self, db):
        self._conn = db
        self._conn.autocommit(False)
        
    def commit(self):
        if self._conn:
            self._conn.commit()
            self._conn.autocommit(True)
        
    def rollback(self):
        if self._conn:
            self._conn.rollback()
            self._conn.autocommit(True)
