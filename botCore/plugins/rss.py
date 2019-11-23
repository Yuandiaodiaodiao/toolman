from nonebot import on_command, CommandSession
from nonebot.typing import Context_T
from nonebot import NoneBot
import nonebot
import nonebot.helpers
import json
import requests
from myConfig.configJson import configJs

import aiohttp

timewait=1
bot = nonebot.get_bot()
# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据

@on_command('#',only_to_me=False)
async def rssMessage(session: CommandSession):
    text = "# "
    # if any(map(lambda x: x.type == 'at' and x.data['qq']==str(ctx['self_id']), ctx['message'])):
    #     ctx['at'] = True
    # if not ctx.get('at'):
    #     return
    text+=session.current_arg_text
    imageList=session.current_arg_images
    print(text)

    data = {
        "qq_group_id": str(session.ctx.get('group_id') or ""),
        "qq_id": str(session.ctx.get('user_id')),
        "text": text,
        "img": imageList,
        "msg_id": str(session.ctx.get('message_id') or "")
    }
    try:
        async with aiohttp.request('POST', f'http://{configJs["serverip"]}:{configJs["rssMessageListen"]}', data=json.dumps(data),timeout=aiohttp.client.ClientTimeout(total=timewait))as r:
            js=await r.text()
            print(js)
            print('finish')
            pass
        # requests.post('http://192.168.137.205:50383',data=json.dumps(data),timeout=3)
    except Exception as e:
        print('rss server error'+str(e))
