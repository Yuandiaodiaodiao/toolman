from nonebot import on_command, CommandSession
from nonebot.typing import Context_T
import nonebot.helpers
import nonebot
bot = nonebot.get_bot()
@bot.on_message('group')
async def handle_group_message(ctx: Context_T):
    text=""
    for i in ctx.get('message'):
        if i.type == 'text':
            text += i.data['text']
