from datetime import datetime
import requests
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
import json
from nonebot.message import MessageSegment, Message


@nonebot.scheduler.scheduled_job('interval', seconds=1)
async def _():
    bot = nonebot.get_bot()

    try:
        pass
        data = {
            'formBot': True
        }
        try:
            res = requests.post('http://127.0.0.1:50382', data=json.dumps(data))
            js = json.loads(res.text)
        except:
            return
        for i in js:
            print(i)
            msg = Message('')
            # int(i.get('qq_group_id'))
            for j in i.get('qq_id_list'):
                msg.append(MessageSegment.at(int(j)))
            msg.extend('\n')
            textObj = i.get('text')
            if isinstance(textObj, list):
                for j in textObj:
                    msg.extend(j.replace('$', ' '))
            else:
                try:
                    msg.extend(i.get('text'))
                except:
                    print(f'i.get() error')
            await bot.send_group_msg(group_id=967636480,
                                     message=msg)
            print('say')
        # await bot.send_group_msg(group_id=967636480,
        #                          message=f'给爬')

    except CQHttpError:
        pass
