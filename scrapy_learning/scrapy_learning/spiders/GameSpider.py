#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy_learning.items import GameItem
"""

@created: 2019/7/17 15:07
@author: huangmin
@copyright: 2019 www.mindasoft.com Inc. All rights reserved.
"""

class CitySpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['y.wan.mgtv.com']
    start_urls = ['http://y.wan.mgtv.com/index.php?view=id2code']
    unionId = 698892

    def start_requests(self):
        # print('start_requests')
        u = 'http://y.wan.mgtv.com/index.php?view=id2code'
        form_data = {
            'id': str(self.unionId),
            'code': '',
            'nickname':  '',
            'uuid':  ''
        }
        yield scrapy.FormRequest(url=u, formdata=form_data, callback=self.parse)

    def parse(self, response):
        # print('parse')
        tbody_data = response.xpath('//div[@class="info-list"]/div[1]/table/tbody')
        # print(tbody_data)
        if len(tbody_data) != 0:
            print("begin%s"% self.unionId)

            unionId = tbody_data.xpath("./tr[1]/td[2]/text()")
            ufrom = tbody_data.xpath("./tr[2]/td[2]/text()")
            nickname = tbody_data.xpath("./tr[3]/td[2]/text()")
            uuid = tbody_data.xpath("./tr[4]/td[2]/text()")
            name = tbody_data.xpath("./tr[5]/td[2]/text()")
            idcard = tbody_data.xpath("./tr[6]/td[2]/text()")
            loginTime = tbody_data.xpath("./tr[7]/td[2]/text()")
            ip = tbody_data.xpath("./tr[8]/td[2]/text()")
            phone = tbody_data.xpath("./tr[9]/td[2]/text()")
            qq = tbody_data.xpath("./tr[11]/td[2]/text()")
            item = GameItem();
            if len(unionId) > 0:
                item['unionId'] = unionId[0].extract()
            else:
                item['unionId'] = ""
            if len(ufrom) > 0:
                item['ufrom'] = ufrom[0].extract()
            else:
                item['ufrom'] = ""
            if len(nickname) > 0:
                item['nickname'] = nickname[0].extract()
            else:
                item['nickname'] = ""
            if len(uuid) > 0:
                item['uuid'] = uuid[0].extract()
            else:
                item['uuid'] = ""
            if len(name) > 0:
                item['name'] = name[0].extract()
            else:
                item['name'] = ""
            if len(idcard) > 0:
                item['idcard'] = "'"+idcard[0].extract()
            else:
                item['idcard'] = ""
            if len(loginTime) > 0:
                item['loginTime'] = loginTime[0].extract()
            else:
                item['loginTime'] = ""
            if len(ip) > 0:
                item['ip'] = ip[0].extract()
            else:
                item['ip'] = ""
            if len(phone) > 0:
                item['phone'] = phone[0].extract()
            else:
                item['phone'] = ""
            if len(qq) > 0:
                item['qq'] = qq[0].extract()
            else:
                item['qq'] = ""
            print(item)
            yield item

        self.unionId = self.unionId + 1
        if self.unionId <= 900000:
            print("next%s"% self.unionId)
            u = 'http://y.wan.mgtv.com/index.php?view=id2code'
            form_data = {
                'id': str(self.unionId),
                'code': '',
                'nickname': '',
                'uuid': ''
            }
            yield scrapy.FormRequest(url=u, formdata=form_data, callback=self.parse)
