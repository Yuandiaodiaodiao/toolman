import feedparser
import json
import requests
from urllib import request

MESSES_NUMBER = 3


def check_url(url):
    with request.urlopen(url) as file:
        print(file.status)
        print(file.reason)
        ans = file.reason
    return ans


fin = open('rss_list.json', encoding='utf-8')
content = fin.read()
json_reader = json.loads(content)
last_mess = {}
for key_i in json_reader.keys():
    for key_j in json_reader[key_i].keys():
        send_package = {}
        rss_reader = feedparser.parse(key_j)
        # print(rss_reader.keys())
        # print(rss_reader['entries'])
        texts = []
        for index, lis in enumerate(rss_reader['entries']):
            if index >= MESSES_NUMBER:
                break
            text = ''
            text = lis['title'] + '$' + lis['link'] + '$' + lis['author']
            if key_j in last_mess:
                if text == last_mess[key_j]:
                    break
            texts.append(text)
        if len(texts) != 0:
            last_mess[key_j] = texts[0]
        send_package['qq_group_id'] = key_i
        send_package['qq_id_list'] = json_reader[key_i][key_j]
        send_package['text'] = texts
        send_package['img'] = ''
        json.dumps(send_package)
        print(send_package)
# print(lis['content'][0].keys())


# qq_group_id, qq_id_list, text, img


# print(lis.keys())
# print(lis['title'])  # 标题
# print(lis['link'])  # 链接
# print(lis['published'])  # 发布时间
#                print(lis['updated'])#更新时间
# print(lis['summary'])  # 简介
#                print(lis['authors'])#作者们的资料
#                print(lis['href'])#形似主页
# print(lis['author'])  # 作者？主作者之类的
