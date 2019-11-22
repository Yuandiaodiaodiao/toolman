import nonebot
import sys
import os
# nowpath=os.path.split(os.path.realpath(__file__))[0]
# sys.path.append("./")
from . import config
from os import path

def run():
    toolmandir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.append(toolmandir)
    toolmandir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(toolmandir)
    nonebot.init(config)
    # nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins'
    )
    nonebot.run(host='0.0.0.0', port=9002)

if __name__ == "__main__":
    run()
