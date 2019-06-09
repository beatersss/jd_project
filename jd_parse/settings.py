# -*- coding: utf-8 -*-

# Scrapy settings for jd_parse project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_parse'

SPIDER_MODULES = ['jd_parse.spiders']
NEWSPIDER_MODULE = 'jd_parse.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd_parse (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection":"keep-alive",
    "Cookie":"__jda=122270672.15595986145001282846923.1559598614.1559655938.1559684767.3; __jdc=122270672; __jdv=122270672|direct|-|none|-|1559598614501; __jdu=15595986145001282846923; areaId=11; ipLoc-djd=11-799-801-32705; PCSYCityID=274; shshshfp=7b2a10f474fdacd2bbfb4ebb3b7aa922; shshshfpa=861d3f26-629f-7b7c-2fcc-24c18a780277-1559598617; shshshfpb=wC%2FqIyy672auK3xMUEY2eUw%3D%3D; 3AB9D23F7A4B3C9B=X24D4RIKSQBAZAVGCZTA6KOU2DGETIZ3BAEL7C6JCGQ3DX4VSIRMOBD6O34OVIE3QDEKJ5KD6F7FBBSLXWOVBLVMT4; _gcl_au=1.1.683942006.1559657115; mt_xid=V2_52007VwMWVlVcWlMYSRxYBGYDEVteUVddF0obbFBlUxRRCghVRhlKTVgZYgQWUkELBlgcVRpVUG8AEwAJUVtZF3kaXQVvHxNVQVlXSxxKEl8AbAESYl9oUmodTB5UA2cAFFptWFReGw%3D%3D; shshshsID=fbe6514313b2cfc4ed8bea075e062527_1_1559684766778; __jdb=122270672.1.15595986145001282846923|3.1559684767",
    "Host":"sclub.jd.com",
    "Referer":"https://item.jd.com/5544068.html",
    "TE":"Trailers",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/67.0",

}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd_parse.middlewares.JdParseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jd_parse.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'jd_parse.pipelines.JdParsePipeline': 300,
    'jd_parse.pipelines.MongoPipeline':300,
    # 'scrapy_redis.pipelines.RedisPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_URI = '192.168.30.11'
MONGO_DATABASE = 'jd_comment'

#分布式 调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# #去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
#
# REDIS_URL = 'redis://root:1234@192.168.30.11:6379/2'
# REDIS_URL = 'redis://192.168.30.11:6379/1'

#选择一个模式,
# 0  爬取该品牌下全部手机型号的评论信息
# 1  爬取指定一个型号的信息
