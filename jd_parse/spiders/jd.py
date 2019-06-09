# -*- coding: utf-8 -*-
import re
import json
import time
import codecs
import requests
from bs4 import BeautifulSoup
import scrapy
from scrapy import Spider,Request


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["www.jd.com"]
    with open("./data/url.txt") as fp:
        temp_list = fp.readlines()
        temp_list = ["https:" + url.split("\t")[0] for url in temp_list]
    start_urls = temp_list#['https://item.jd.com/5544068.html']  #score #0:全部评价  1:差评  2:中评  3:好评
    comment_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1&productId={productId}&score={score}&sortType=5&page={page}&pageSize=10&isShadowSku=0&fold=1'
    productId = ""

    def start_requests(self):
        for url in self.start_urls:
            self.productId = url.split("/")[-1].split(".")[0]
            for score in range(4):
                page = 0
                while page < 100:
                    yield Request(self.comment_url.format(productId=self.productId,score=score,page=page),self.parse,dont_filter=True)
                    page += 1
                    time.sleep(1)


    def parse(self, response):
        print('--->',response.text)
        # result = re.sub('fetchJSON_comment98vv6955\(','',response.text)
        # result = re.sub('\);', '', result)
        temp_len = response.text.index("(") + 1
        result = response.text[temp_len:]
        result = result[:-2]
        with codecs.open("./comments/%s.csv"%self.productId,mode='a+',encoding='utf8') as fp:
            fp.write(result+"\n")




