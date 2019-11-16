from nonebot import on_command, CommandSession
from nonebot.message import Message, MessageSegment


@on_command('抽象矩阵')
async def colorImage(session: CommandSession):
    # 获取城市的天气预报
    # 向用户发送天气预报
    target=session.current_arg_text.strip()
    msg = ""
    await session.send(msg)
