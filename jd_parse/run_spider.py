#!/usr/bin/env python
# encoding: utf-8
'''
@author: taiyc
@file: run_spider
@time: 2019/3/29 21:44
'''

from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'jd'])