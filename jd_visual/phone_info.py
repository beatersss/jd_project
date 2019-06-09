#-*-encoding:utf8-*-
# 爬取手机详细信息
import requests
from bs4 import BeautifulSoup
import time
import codecs
headers = {
    "Host": "item.jd.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie":"__jda=122270672.15595986145001282846923.1559598614.1559598614.1559655938.2; __jdc=122270672; __jdv=122270672|direct|-|none|-|1559598614501; __jdu=15595986145001282846923; areaId=11; ipLoc-djd=11-799-801-32705; PCSYCityID=274; shshshfp=7b2a10f474fdacd2bbfb4ebb3b7aa922; shshshfpa=861d3f26-629f-7b7c-2fcc-24c18a780277-1559598617; shshshfpb=wC%2FqIyy672auK3xMUEY2eUw%3D%3D; shshshsID=38fc50668d8c19cf91e181b75938aa6a_6_1559659257105; __jdb=122270672.13.15595986145001282846923|2.1559655938; 3AB9D23F7A4B3C9B=X24D4RIKSQBAZAVGCZTA6KOU2DGETIZ3BAEL7C6JCGQ3DX4VSIRMOBD6O34OVIE3QDEKJ5KD6F7FBBSLXWOVBLVMT4; _gcl_au=1.1.683942006.1559657115; mt_xid=V2_52007VwMWVlVcWlMYSRxYBGYDEVteUVddF0obbFBlUxRRCghVRhlKTVgZYgQWUkELBlgcVRpVUG8AEwAJUVtZF3kaXQVvHxNVQVlXSxxKEl8AbAESYl9oUmodTB5UA2cAFFptWFReGw%3D%3D",
    "Upgrade-Insecure-Requests": "1"
}

with open("./data/url.txt") as fp:
    temp_list = fp.readlines()
    temp_list = ["https:"+url.split("\t")[0] for url in temp_list ]

for url in temp_list:
    # url = "https://item.jd.com/46248089667.html"
    productId = url.split("/")[-1].split(".")[0]
    r = requests.get(url,headers=headers)
    data = BeautifulSoup(r.text)
    fp = codecs.open("./data/info/%s_info.txt"%productId,mode='w+',encoding='utf8')

    cate =  data.find("div",class_="head").find('a').text.strip()
    print cate
    phone_info = data.find("ul",class_="parameter2 p-parameter-list").find_all("li")
    fp.write(u"cate：%s\n"%cate)
    for info in phone_info:
        fp.write(info.text+'\n')
    fp.close()
    print url,phone_info
    time.sleep(1)