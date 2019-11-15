import feedparser
import json

fin = open('rss_list.json', encoding='utf-8')
content = fin.read()
jsonreader = json.loads(content)
for List in jsonreader:
    for j in List:
        if j == 'url':
            rssreader = feedparser.parse(List[j])
            print(rssreader.keys())
            for key in rssreader.keys():
                print(rssreader[key])
#print(jsonreader)
