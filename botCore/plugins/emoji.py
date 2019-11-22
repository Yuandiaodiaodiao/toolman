from nonebot import on_command, CommandSession
from nonebot.message import Message, MessageSegment
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

@on_command('抽象矩阵')
async def colorImage(session: CommandSession):
    # 获取城市的天气预报
    # 向用户发送天气预报
    targetList=session.current_arg_text.strip().split()
    target=targetList[0]
    text = bytes(target, encoding='unicode_escape')
    text = str(text).replace("'", '').replace("\\", '').split('U')
    emojiId = int(text[1], 16)
    colorEmoji = []
    if emojiId >= 0x1F466 and emojiId <= 0x1F478 or True:
        colorEmoji.append(chr(emojiId))
        for i in range(0x1f3fb, 0x1f3ff + 1):
            newchar = chr(emojiId) + chr(i)
            # print(newchar)
            colorEmoji.append(newchar)

    colorEmoji = colorEmoji[0:5]
    try:
        colorEmoji = colorEmoji[0:int(targetList[1])]
    except:
        pass
    colorEmoji.reverse()
    eList = mat_put(colorEmoji)
    # text=text.decode('unicode_escape')
    text = ""
    for i in eList:
        for j in i:
            text += j
        text += '\n'
    text=text.strip('\n')

    # newchar=chr(0x1F468)+chr(0x0200D)+chr(0x1F467)
    msg =text
    await session.send(msg)
