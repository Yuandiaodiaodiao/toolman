from nonebot import on_command, CommandSession
from nonebot.message import Message,MessageSegment
import screepsapi
USER = "Yuandiaodiaodiao"
PASSWORD = ""

# on_command 装饰器将函数声明为一个命令处理器
# @机器人 支援 E25N43 power 1000
@on_command('支援')
async def screeps(session: CommandSession):
    command=session.current_arg_text.strip().split(" ")
    apii = screepsapi.API(USER, PASSWORD, host="screeps.com", secure=True)
    try:
        num=int(int(command[2])/10)
        if num>6000:
            await session.send('爬爬爬')
            return
        commad=f"Game.tools.give('{command[0]}','{command[1]}',{str(num)})"
        print('------------------------------支援指令='+commad)
        res = apii.console(commad, shard='shard3')
    except:

        pass
    if apii is not None:
        del apii
    await session.send('ok')