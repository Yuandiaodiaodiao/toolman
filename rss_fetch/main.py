import feedparser
import time
import json
import re
import requests
from urllib import request
import datetime
import socket
MESSES_NUMBER = 1
IP_ADDRESS = 'http://192.168.137.1:50382'
RSSHUB_URL = "https://rsshub.app"
OUT_RSSHUB_URL = "http://server.oops-sdu.cn:1200"
socket.setdefaulttimeout(5)

def check_url(url):
    with request.urlopen(url) as file:
        print(file.status)
        print(file.reason)
        ans = file.reason
    return ans


last_mess = {}
while True:
    print('新的一轮', datetime.datetime.now())
    with open('rss_list.json', encoding='utf-8') as fin:
        content = fin.read()
    json_reader = json.loads(content)
    for key_i in json_reader.keys():
        for key_j in json_reader[key_i].keys():
            send_package = {}
            print(key_j.replace(RSSHUB_URL, OUT_RSSHUB_URL))
            rss_reader = feedparser.parse(key_j.replace(RSSHUB_URL, OUT_RSSHUB_URL))
            # print(rss_reader.keys())
            # print(rss_reader['feed'])
            texts = []
            picture = []
            is_pxj = re.search('bilibili', key_j)
            is_ryf = re.search('ruanyifeng', key_j)
            is_sdu = re.search('sdu/cs', key_j)
            for index, lis in enumerate(rss_reader['entries']):
                if index >= MESSES_NUMBER:
                    break
                text = ''
                text = rss_reader['feed']['title'] + '👇\n' + lis['title'] + '\n' + lis['link']
                # if 'author' in lis:
                #     text = text + '\n' + lis['author']
                if is_pxj:
                    # print('this is summary ' + lis['summary'])
                    img_pos_l = re.search('img src="', lis['summary']).span()[1]
                    img_pos_r = re.search('.jpg', lis['summary']).span()[1]
                    picture.append(lis['summary'][img_pos_l:img_pos_r])
                elif is_ryf:
                    img_pos_l = re.search('img src="', lis['content'][0]['value']).span()[1]
                    img_pos_r = re.search('.jpg', lis['content'][0]['value']).span()[1]
                    picture.append(lis['content'][0]['value'][img_pos_l:img_pos_r])
                # elif is_sdu:
                # print(lis)
                if key_i + key_j in last_mess:
                    if text == last_mess[key_i + key_j]:
                        break
                texts.append(text)
            if len(texts) != 0:
                last_mess[key_i + key_j] = texts[0]
                send_package['qq_group_id'] = key_i
                send_package['qq_id_list'] = json_reader[key_i][key_j]
                send_package['text'] = texts
                send_package['img'] = picture
                res = requests.post(IP_ADDRESS, data=json.dumps(send_package))
                print(send_package)
    time.sleep(5)
# print(lis['content'][0].keys())


# qq_group_id, qq_id_list, text, img


# print(lis.keys())
# print(lis['title'])  # 标题
# print(lis['link'])  # 链接
# print(lis['published'])  # 发布时间
# print(lis['updated'])#更新时间
# print(lis['summary'])  # 简介
# print(lis['authors'])#作者们的资料
# print(lis['href'])#形似主页
# print(lis['author'])  # 作者？主作者之类的
