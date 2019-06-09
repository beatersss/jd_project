
# 数据处理模块

path = "./data/"
import os
import json
import codecs
null = ""
true = True
false = False

comments_dict = {}

def analysisJson(temp = {}):
    comments = temp['comments']
    comment_dict2 = {}
    comment_dict2['creationTime'] = []
    comment_dict2['content'] = []
    comment_dict2['score'] = []
    for com in comments:
        comment_dict2['creationTime'].append(com['creationTime'])
        comment_dict2['content'].append(com['content'])
        comment_dict2['score'].append(com['score'])
    return comment_dict2

def comments(fn = "1861102.csv",comments_dict= {}):

    fname = fn.split(".")[0]
    with codecs.open("./data/back_data/%s"%fn,mode='r',encoding='utf8') as fp:
        temp_list = fp.readlines()
    comments_dict[fname] = {}
    comments_dict[fname]['creationTime'] = []
    comments_dict[fname]['content'] = []
    comments_dict[fname]['score'] = []
    for temp in temp_list:
        temp = json.loads(temp.strip())
        temp_dict = analysisJson(temp=dict(temp))
        # print(temp_dict)
        comments_dict[fname]['creationTime'] += temp_dict['creationTime']
        comments_dict[fname]['content'] += temp_dict['content']
        comments_dict[fname]['score'] += temp_dict['score']
    return comments_dict

def extractPhonInfo():
    info_dict = {}
    info_detail_dict = {}
    for fn in os.listdir("./data/info"):
        fname = fn.split("_")[0]
        with codecs.open('./data/info/%s'%fn,encoding='utf8') as fp:
            result = fp.readlines()
            result = [res.split("\n")[0] for res in result]
        info_detail_dict[fname] = result
        if len(result)>0:
            info_dict[result[1].split("：")[1]] = fname

    return info_dict,info_detail_dict

def simliar(v1="abc",v2='bcd'):
    v1_list = list(v1)
    v2_list = list(v2)
    return len(list(set(v1_list)&set(v2_list)))/float(len(list(set(v1_list)))+len(list(set(v2_list))))

def getPrice():
    price_dict = {}
    with open("./data/url.txt",mode='r') as fp:
        result = fp.readlines()
        result =[res.strip().split("\t") for res in result]
    for k,v in result:
        k = k.split("/")[-1].split(".")[0]
        price_dict[k] = v
    return price_dict
# comments_dict = comments(comments_dict = comments_dict)
info_dict,info_detail_dict = extractPhonInfo()
price_dict = getPrice()
if __name__ == "__main__":
    getPrice()
    # print(comments('1861102.csv',comments_dict = comments_dict)['1861102']['content'])
    # print(comments_dict)
    # print(simliar())
    # print(list(info_dict.keys()))