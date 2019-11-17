from nonebot import on_command, CommandSession
from nonebot.message import Message,MessageSegment
import nonebot
from os import path
# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('重载a')
async def reload(session: CommandSession):
    nonebot.load_plugins(
        path.join(path.dirname(__file__),''),
        'plugins'
    )
    await session.send('模块重载')