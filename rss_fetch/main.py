import feedparser
import json
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
for List in json_reader:
    last_mess = {}
    for j in List:
        if j == 'url':
            rss_reader = feedparser.parse(List[j])
            print(rss_reader.keys())
            #           print(rss_reader['entries'])
            texts = []
            for index, lis in enumerate(rss_reader['entries']):
                if index >= MESSES_NUMBER:
                    break
                text = ''
                text = lis['title'] + '$' + lis['link'] + '$' + lis['published'] + '$' + lis['summary'] + '$' + lis['author']
                if text == last_mess[List[j]]:
                    break
                texts.append(text)
            last_mess[List[j]] = texts[0]
#                print(lis['content'][0].keys())



#qq_group_id, qq_id_list, text, img




#print(lis.keys())
#print(lis['title'])  # 标题
#print(lis['link'])  # 链接
#print(lis['published'])  # 发布时间
#                print(lis['updated'])#更新时间
#print(lis['summary'])  # 简介
#                print(lis['authors'])#作者们的资料
#                print(lis['href'])#形似主页
#print(lis['author'])  # 作者？主作者之类的