from nonebot import on_command, CommandSession
from nonebot.message import Message, MessageSegment
import aiohttp
import ab

@on_command('和我对线')
async def abWord(session: CommandSession):
    async with aiohttp.request('GET', 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn') as r:
        js = await r.text()
        js=ab.str2abs(js)
    await session.send(js)
