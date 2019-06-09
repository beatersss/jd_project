# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import csv

class JdParsePipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    def __init__(self):
        self.f = open("wangyiyun.csv", "a+")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['id', 'song', 'nickname', 'avatarurl','hotcomment_like','comments'])

    def process_item(self, item, spider):
        wangyiyun_list =  [item['id'], item['song'], item['nickname'], item['avatarurl'],item['hotcomment_like'], item['comments']]

        self.writer.writerow(wangyiyun_list)
        return item
    def close_spider(self, spider):#关闭
        self.writer.close()
        self.f.close()