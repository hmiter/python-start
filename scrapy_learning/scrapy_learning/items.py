# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLearningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    addr = scrapy.Field()
    name = scrapy.Field()


class CityItem(scrapy.Item):
    name = scrapy.Field()
    code = scrapy.Field()


class GameItem(scrapy.Item):
    unionId = scrapy.Field()
    uuid = scrapy.Field()
    nickname = scrapy.Field()
    name = scrapy.Field()
    idcard = scrapy.Field()
    ufrom = scrapy.Field()
    phone = scrapy.Field()
    loginTime = scrapy.Field()
    ip = scrapy.Field()
    qq = scrapy.Field()
