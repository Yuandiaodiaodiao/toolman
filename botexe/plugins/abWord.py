from tool.tools import emojiToHex
import ab
from nonebot import on_command, CommandSession
from nonebot.message import Message, MessageSegment

@on_command('抽象话')
async def abWord(session: CommandSession):
    targetList=session.current_arg_text.strip()
    msg=ab.str2abs(targetList)
    await session.send(msg)
