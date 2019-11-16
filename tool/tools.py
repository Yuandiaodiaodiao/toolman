def emojiToHex(target):
    text = bytes(target, encoding='unicode_escape')
    text = str(text).replace("'", '').replace('b','').replace("\\", '').split('U')
    emojiList =[int(i, 16) for i in text if len(i)>0]
    return emojiList
def spliteEmoji(emojiList):
    emojiList=emojiToHex(emojiList)
    emojiArray=[]
    temp = []
    for x in emojiList:
        if x>=0x1F3FB and x<=0x1F3FF:
            temp.append(x)
            emojiArray.append(temp)
            temp=[]
        elif x==0xfe0f or x==0xfe0e:
            temp.append(x)
            emojiArray.append(temp)
            temp = []
        elif x>=0x1f1e6 and x<=0x1f1e6+25:
            temp.append(x)
            if len(temp)==2:
                emojiArray.append(temp)
                temp = []
        elif x==0x0200D:
            # emojiArray.append(temp)
            temp=[]
        elif len(temp)==0:
            temp.append(x)
        else:
            temp.append(x)
            emojiArray.append(temp)
            temp = []
