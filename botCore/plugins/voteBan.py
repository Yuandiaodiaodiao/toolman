import aiohttp
from nonebot.message import Message, MessageSegment
import nonebot
from nonebot import on_command, CommandSession
from nonebot.natural_language import on_natural_language, NLPSession, NLPResult, IntentCommand
from nonebot.permission import *

banList = {}
banConfig = {
    '967636480': 3
}


@on_natural_language(keywords={'投票禁言'})
async def _(session: NLPSession):
    return IntentCommand(50.0, ('投票禁言',), None)


@on_command('投票禁言', permission=GROUP | DISCUSS)
async def banVote(session: CommandSession):
    banQQ = None
    for x in session.ctx['message']:
        if x.type == 'at':
            banQQ = x.data['qq']
    if banQQ is None:
        return
    groupId = session.ctx['group_id']
    if banList.get(groupId) is None:
        banList[groupId] = {}
    groupBanList = banList[groupId]
    if groupBanList.get(banQQ) is None:
        groupBanList[banQQ] = []
    usrId = session.ctx.get('user_id')
    if usrId not in groupBanList[banQQ]:
        groupBanList[banQQ].append(usrId)
        limit = banConfig.get(str(groupId))
        bot = nonebot.get_bot()
        if limit is None:
            try:
                info = await bot.get_group_info(group_id=groupId)
                limit = info.get('member_count') // 3
            except CQHttpError as e:
                pass
                return
        msg = Message()
        try:
            info = await bot.get_group_member_info(group_id=groupId, user_id=banQQ)
        except CQHttpError as e:
            pass
            return

        msg.extend(f"投票对{info.get('nickname')}的禁言{len(groupBanList[banQQ])}/{limit}")
        await session.send(msg)
        if len(groupBanList[banQQ]) >= limit:
            try:
                info = await bot.set_group_ban(group_id=groupId, user_id=banQQ, duration=60 * limit)
                groupBanList[banQQ] = None
            except CQHttpError as e:
                pass
                return
