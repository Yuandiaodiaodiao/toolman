from nonebot import on_command, CommandSession
from nonebot.message import Message,MessageSegment

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('无内鬼', aliases=('色图','a'))
async def colorImage(session: CommandSession):
    # 获取城市的天气预报
    # 向用户发送天气预报
    msg=Message()
    url="http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%89%B2%E5%9B%BE"
    imgurl='https://s2.ax1x.com/2019/03/29/A00Whn.png'
    # msg.append(MessageSegment.share(url,"色图","网警已介入本群",imgurl))
    msg.append(MessageSegment.image('https://s2.ax1x.com/2019/11/16/MBYbmd.jpg'))
    msg.extend('没有色图给👴爬')
    await session.send(msg)