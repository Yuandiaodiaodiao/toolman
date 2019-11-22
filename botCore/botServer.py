import nonebot
import sys
import os
# nowpath=os.path.split(os.path.realpath(__file__))[0]
# sys.path.append("./")
try:
    from . import config
except:
    try:
        import config
    except:
        print('config error')
from os import path
from myConfig.configJson import configJs


def run():
    # toolmandir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # sys.path.append(toolmandir)
    toolmandir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(toolmandir)
    nonebot.init(config)
    # nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(os.path.abspath(__file__)), 'plugins'),
        'plugins'
    )
    nonebot.run(host='0.0.0.0', port=configJs['nonebotListen'])


if __name__ == "__main__":
    run()
