# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib,urllib2

import os


class ScrapyLearningPipeline(object):
    def process_item(self, item, spider):
        return item


class PicPipeline(object):
    def process_item(self, item, spider):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        req = urllib2.Request(url=item['addr'], headers=headers)
        res = urllib2.urlopen(req)
        file_name = os.path.join(r'E:\down_pic', item['name'] + '.jpg')
        with open(file_name, 'wb') as fp:
            fp.write(res.read())


class CytyPipeline(object):
    def process_item(self, item, spider):
        file_name = os.path.join(r'E:\down_pic', 'city' + '.csv')
        with open(file_name, 'a+') as fp:
            fp.write(item['name'] + "," + item['code'])
            fp.write('\n')


class GamePipeline(object):
    def process_item(self, item, spider):
        unionId = int(item['unionId'])
        idx = unionId//100000

        file_name = os.path.join(r'E:\\', 'game' + str(idx) + '.csv')
        print("write begin:" + str(file_name))
        with open(file_name, 'a+') as fp:
            line = item['unionId'] + ","  + item['uuid'] + "," +  item['idcard'] + "," + item['loginTime'] + "," + item['ip'] + "," + item['phone'] + "," + item['qq'] +'\n'
            # print(line)
            fp.write(line)
            print("write finish")
