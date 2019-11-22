from nonebot import on_command, CommandSession
from nonebot.message import Message,MessageSegment
import nonebot
from os import path
import sys
import os

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    print('ready to restart program......')
    python = sys.executable
    os.execl(python, python, *sys.argv)


@on_command('重载模块')
async def reload(session: CommandSession):
    nonebot.load_plugins(
        path.join(path.dirname(__file__),''),
        'plugins'
    )

    await session.send('模块重载')
    restart_program()

