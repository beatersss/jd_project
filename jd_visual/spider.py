#-*-encoding:utf8-*-
# 爬取连接 和 价格信息
import requests
from bs4 import BeautifulSoup
import time
import json
headers = {
    "Host": "list.jd.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://shouji.jd.com/",
    "Cookie":"__jda=122270672.15595986145001282846923.1559598614.1559598614.1559655938.2; __jdc=122270672; __jdv=122270672|direct|-|none|-|1559598614501; __jdu=15595986145001282846923; areaId=11; ipLoc-djd=11-799-801-32705; PCSYCityID=274; shshshfp=e630c3cceba3b190226e8354d291b7c0; shshshfpa=861d3f26-629f-7b7c-2fcc-24c18a780277-1559598617; shshshfpb=wC%2FqIyy672auK3xMUEY2eUw%3D%3D; listck=f9537e62659fb6f8442411658366a917; shshshsID=38fc50668d8c19cf91e181b75938aa6a_3_1559657087445; __jdb=122270672.8.15595986145001282846923|2.1559655938; 3AB9D23F7A4B3C9B=X24D4RIKSQBAZAVGCZTA6KOU2DGETIZ3BAEL7C6JCGQ3DX4VSIRMOBD6O34OVIE3QDEKJ5KD6F7FBBSLXWOVBLVMT4; _gcl_au=1.1.683942006.1559657115",
    "Upgrade-Insecure-Requests": "1"
}
fp = open("./data/url.txt",mode='w+')
for page in range(2,100):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=%s&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=8#J_main"%page
    r = requests.get(url,headers=headers)
    data = BeautifulSoup(r.text)

    for text in data.find_all("li",class_="gl-item"):
        p_name = text.find('div',class_="p-name").find("a")['href']
        item_id = p_name.split("/")[-1].split(".")[0]
        url = "https://p.3.cn/prices/mgets?callback=jQuery%s&skuids=J_%s"%(item_id,item_id)
        price = requests.get(url).text
        temp_len = len("jQuery%s(["%item_id)
        time.sleep(1)
        price = json.loads(price[temp_len:-4])['p']
        print p_name,price
        fp.write(p_name+"\t"+price+'\n')
        print"-------------------------------------------"
    time.sleep(3)