# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MyspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='',port=3306,db='auth',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT into t_news(title,content)VALUES(%s,%s)'
        self.cursor.execute(sql,(item['title'],item['info']))
        self.conn.commit()
        return item
		
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
