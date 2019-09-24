# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_learning.items import CityItem

"""
获取统计局行政单位编码
@created: 2019/6/13 13:52
@author: huangmin
@copyright: 2019 www.mindasoft.com Inc. All rights reserved.
"""

class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html']
    url_set = set()

    def parse(self, response):
        if response.url == "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html":
            allProvincetr = response.xpath('//tr[@class="provincetr"]/td')
            for city in allProvincetr:
                item = CityItem()
                name = city.xpath('./a/text()').extract()[0]
                code = city.xpath('./a/@href').extract()[0]
                item['name'] = name
                item['code'] = code.replace(".html","0000000000")
                # 返回爬取到的信息
                yield item
        else:
            if re.match("^http([\d\D]*)2018/\d*.html$", response.url):
                allCitys = response.xpath('//tr[@class="citytr"]')
                for city in allCitys:
                    item = CityItem()
                    name = city.xpath('./td[2]/a/text()').extract()
                    code = city.xpath('./td[1]/a/text()').extract()
                    if len(name) == 0:
                        name = city.xpath('./td[2]/text()').extract()
                        code = city.xpath('./td[1]/text()').extract()

                    item['name'] = name[0]
                    item['code'] = code[0]
                    # 返回爬取到的信息
                    yield item
            elif re.match("^http([\d\D]*)2018/\d*/\d*.html$", response.url):
                allCountys = response.xpath('//tr[@class="countytr"]')
                for county in allCountys:
                    item = CityItem()
                    name = county.xpath('./td[2]/a/text()').extract()
                    code = county.xpath('./td[1]/a/text()').extract()
                    if len(name) == 0:
                        name = county.xpath('./td[2]/text()').extract()
                        code = county.xpath('./td[1]/text()').extract()

                    item['name'] = name[0]
                    item['code'] = code[0]
                    # 返回爬取到的信息
                    yield item
            elif re.match("^http([\d\D]*)2018/\d*/\d*/\d*.html$", response.url):
                allTowns = response.xpath('//tr[@class="towntr"]')
                for town in allTowns:
                    item = CityItem()
                    name = town.xpath('./td[2]/a/text()').extract()
                    code = town.xpath('./td[1]/a/text()').extract()
                    if len(name) == 0:
                        name = town.xpath('./td[2]/text()').extract()
                        code = town.xpath('./td[1]/text()').extract()

                    item['name'] = name[0]
                    item['code'] = code[0]
                    # 返回爬取到的信息
                    yield item
            elif re.match("^http([\d\D]*)2018/\d*/\d*/\d*/\d*.html$", response.url):
                allVillages = response.xpath('//tr[@class="villagetr"]')
                for village in allVillages:
                    item = CityItem()
                    name = village.xpath('./td[3]/text()').extract()
                    code = village.xpath('./td[1]/text()').extract()

                    item['name'] = name[0]
                    item['code'] = code[0]
                    # 返回爬取到的信息
                    yield item

        # 循环
        for next_page in response.xpath('//table//table//a/@href').extract():
            url = response.urljoin(next_page)
            if url in CitySpider.url_set:
                pass
            else:
                CitySpider.url_set.add(url)
                yield scrapy.Request(url, callback=self.parse)
                # yield self.make_requests_from_url(url)
