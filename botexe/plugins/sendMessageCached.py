from datetime import datetime
import requests
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
import json

@nonebot.scheduler.scheduled_job('interval',seconds=5)
async def _():
    bot = nonebot.get_bot()

    try:
        pass
        data={
            'formBot':True
        }
        res=requests.post('127.0.0.1:50382',data=json.dumps(data))
        js=json.loads(res.text)

        # await bot.send_group_msg(group_id=967636480,
        #                          message=f'给🕺🕺🕺爬')
    except CQHttpError:
        pass