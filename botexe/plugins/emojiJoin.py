from tool.tools import emojiToHex

from nonebot import on_command, CommandSession
from nonebot.message import Message, MessageSegment

@on_command('抽象拼接')
async def colorImage(session: CommandSession):

    targetList=session.current_arg_text.strip().replace(' ','')

    str=''
    for index,target in enumerate(targetList):
        emojiList=emojiToHex(target)
        temp=''
        if index>0:
            temp=chr(0x200d)
        for x in emojiList:
            temp+=chr(x)
        str+=temp

    # str=chr(0x1f468)+chr(0x200d)+chr(0x1f468)+chr(0x200d)+chr(0x1f467)+chr(0x200d)+chr(0x1f466)
    msg = str
    await session.send(msg)
