
## Scrapy 爬取京东商城手机评论/

第一步  运行./jd_visual/spider.py
先爬取每个手机的链接 写入到 ./jd_visual/data/url.txt文件当中

第二步 运行./jd_visual/phone_info.py
获取每个具体手机的 商品信息,并以每一个商品id保存一个文件，将其保存在./jd_visual/data/info文件夹下

第三步 运行./jd_parse/spiders/jd.py
获取每个手机下面的评论，每个评论一个文件，文件名称为商品id，并将其存放在 ./jd_parse/comments下

第四步 ./jd_parse/comments将文件下所有文件 放到./jd_visual/data/back_data文件夹下

第五步 运行./jd_visual/tk_ploy.py文件，可以查询手机信息

快速方法 直接解压./jd_visual/data.zip文件然后运行第五步即可