from nonebot import on_command, CommandSession
from nonebot.message import Message, MessageSegment
import aiohttp
import json
import bs4


async def getImage(keyword, limit=1):
    array = []
    param = {
        'keyword': keyword
    }
    async with aiohttp.request('GET', 'http://www.doutula.com/search', params=param) as r:
        js = await r.text()
    soup = bs4.BeautifulSoup(js, "lxml")
    img = soup.find_all('img')
    msg = Message()
    for x in img:
        if x.attrs.get('data-backup'):
            array.append(x.attrs.get('data-backup'))
            limit -= 1
            if limit == 0:
                break
    return array


@on_command('表情包')
async def abWord(session: CommandSession):
    target = session.current_arg_text.strip()
    imageList = await getImage(target)
    msg = Message()
    for x in imageList:
        msg.append(MessageSegment.image(x))
    await session.send(msg)


@on_command('表情包私发')
async def abWord(session: CommandSession):
    target = session.current_arg_text.strip()
    imageList = await getImage(target,5)
    for x in imageList:
        msg = Message()
        msg.append(MessageSegment.image(x))
        await session.send(msg, ensure_private=True)
