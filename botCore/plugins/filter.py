from nonebot import CQHttpError
from nonebot.typing import Context_T
import nonebot
from dfaMaster import check_sensitive
bot = nonebot.get_bot()
@bot.on_message('group')
async def handle_group_message(ctx: Context_T):
    text=""
    for i in ctx.get('message'):
        if i.type == 'text':
            text += i.data['text']

    ifDangerous = check_sensitive(text)
    try:
      pass
    except:
        print('dfa error')
        return
    if ifDangerous :
        text='危险言论'
        try:
            pass
            info = await bot.delete_msg(message_id=ctx['message_id'])
        except CQHttpError:
            pass
        # await nonebot.helpers.send(bot=bot, ctx=ctx, message=text)