from datetime import datetime
import requests
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
import json
from nonebot.message import MessageSegment, Message
import aiohttp
timeWait=2
@nonebot.scheduler.scheduled_job('interval', seconds=timeWait)
async def sendMessageCached():
    bot = nonebot.get_bot()
    try:
        pass
        data = {
            'formBot': True
        }
        try:

            async with aiohttp.request('POST', 'http://127.0.0.1:50382', data=json.dumps(data),timeout=aiohttp.client.ClientTimeout(total=timeWait-1))as r:
                js = await r.text()
                js = json.loads(js)
            # res = requests.post('http://127.0.0.1:50382', data=json.dumps(data),timeout=3)
            # js = json.loads(res.text)
            # print('messcache')
        except:
            return
        for i in js:
            print(i)
            msg = Message('')
            # int(i.get('qq_group_id'))
            for j in i.get('qq_id_list'):
                msg.append(MessageSegment.at(int(j)))
            if len(i.get('qq_id_list')) > 0:
                msg.extend('\n')
            textObj = i.get('text')
            if isinstance(textObj, list):
                for j in textObj:
                    msg.extend(j.replace('$', ' '))
            else:
                try:
                    msg.extend(textObj)
                except:
                    print(f'i.get() error')
            imageList = i.get('img')
            if isinstance(imageList, list):
                for j in imageList:
                    if len(j) > 0:
                        msg.append(MessageSegment.image(j))
            else:
                try:
                    if len(imageList) > 0:
                        msg.append(MessageSegment.image(imageList))
                except:
                    print(f'image send error')
            await bot.send_group_msg(group_id=int(i.get('qq_group_id')),
                                     message=msg)
        # await bot.send_group_msg(group_id=967636480,
        #                          message=f'给爬')

    except CQHttpError:
        pass
