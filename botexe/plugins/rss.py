from nonebot import on_command, CommandSession
from nonebot.typing import Context_T
from nonebot import NoneBot
import nonebot
from messages.handler import handler
import nonebot.helpers

bot = nonebot.get_bot()


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    # 获取城市的天气预报
    weather_report=' 1'
    # 向用户发送天气预报
    await session.send(weather_report)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据

@bot.on_message('group')
async def handle_group_message(ctx: Context_T):
    print(ctx)
    text = ""
    if any(map(lambda x: x.type == 'at' and x.data['qq']==str(ctx['self_id']), ctx['message'])):
        ctx['at'] = True
    if not ctx.get('at'):
        return
    for i in ctx.get('message'):
        if i.type == 'text':
            text += i.data['text']
    data = {
        "qq_group_id": str(ctx.get('group_id')),
        "qq_id": str(ctx.get('user_id')),
        "text": text,
        "img": ''
    }

    ret = handler(data)
    if str(ctx.get('group_id')) == '967636480':
        await nonebot.helpers.send(bot=bot, ctx=ctx, message='handle return ' + str(ret))


from nonebot.message import message_preprocessor



# on_command 装饰器将函数声明为一个命令处理器
# # 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
# @on_command('weather', aliases=('天气', '天气预报', '查天气'))
# async def weather(session: CommandSession):
#     # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
#     city = session.get('city', prompt='你想查询哪个城市的天气呢？')
#     # 获取城市的天气预报
#
#     # 向用户发送天气预报
#     await session.send(weather_report)
#
#
# # weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# # 命令解析器用于将用户输入的参数解析成命令真正需要的数据
# @weather.args_parser
# async def _(session: CommandSession):
#     # 去掉消息首尾的空白符
#     stripped_arg = session.current_arg_text.strip()
#
#     if session.is_first_run:
#         # 该命令第一次运行（第一次进入命令会话）
#         if stripped_arg:
#             # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
#             # 例如用户可能发送了：天气 南京
#             session.state['city'] = stripped_arg
#         return
#
#     if not stripped_arg:
#         # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
#         # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
#         session.pause('要查询的城市名称不能为空呢，请重新输入')
#
#     # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
#     session.state[session.current_key] = stripped_arg
