# -*- coding: utf-8 -*-
import scrapy
from  mySpider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['zhibo8.cc']
    #start_urls = ['https://new.qq.com/cmsn/20190104/20190104010989.html']
    start_urls = ['https://news.zhibo8.cc/nba/']

    def parse(self, response):
        print('+++++++++++++++++')
        for sel in response.xpath('//*[@id="middle"]/div[1]/div[3]/div[2]/ul[1]/li'):
	        # 获取网站标题
            print('============')
            item = MyspiderItem()
            #context = response.xpath('/html/body/div[3]/div[1]/h1/text()')
            title = sel.xpath('a/text()').extract()[0]
            
            item['title'] = title
            item['info'] ='xxx'
            yield item
