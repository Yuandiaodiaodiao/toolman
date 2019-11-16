import json
import requests
def mat_put(a):
    n = len(a)
    l = n * 2 - 1
    listl = [[0] * l for i in range(l)]
    for i in range(0, l):
        for j in range(0, l):
            for k in range(0,n):
                if i == k or i == l - k - 1 or j == k or j == l - k - 1:
                    listl[i][j] = a[k]
                    break
    return listl

def genEmojiMatrix(emojiList):
    eLen = len(emojiList) * 2 - 1
    eList = [[0] * eLen for i in range(eLen)]
    for index,item in enumerate(emojiList):
        for i in range(eLen):
            for j in range(eLen):
                if i==index or j==index:
                    eList[i][j]=emojiList[index]
    return eList

data = {
    'qq_group_id': '967636480',
    'qq_id_list': [],
    'text': '👴',
    'img': ''
}
text = '👴'
text = '👴🏾'
text = bytes(text, encoding='unicode_escape')
text = str(text).replace("'", '').replace("\\", '').split('U')
emojiId = int(text[1], 16)
colorEmoji = []
if emojiId >= 0x1F466 and emojiId <= 0x1F478:
    colorEmoji.append(chr(emojiId))
    for i in range(0x1f3fb, 0x1f3ff + 1):
        newchar = chr(emojiId) + chr(i)
        # print(newchar)
        colorEmoji.append(newchar)
colorEmoji=colorEmoji[0:5]
colorEmoji.reverse()
eList=mat_put(colorEmoji)
# text=text.decode('unicode_escape')
text=""
for i in eList:
    for j in i:
      text+=j
    text+='\r'
# print(text)
# text = ''.join(colorEmoji)
# with open('./plugins/emoji.txt','r',encoding='utf8')as f:
#     text=f.read()
data['text'] = text
# text=text.encode('utf8')
res = requests.post('http://127.0.0.1:50382', data=json.dumps(data))
