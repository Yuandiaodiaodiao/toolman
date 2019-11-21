import nonebot
import sys
import os
# nowpath=os.path.split(os.path.realpath(__file__))[0]
# sys.path.append("./")
import config
from os import path


if __name__ == "__main__":
    sys.path.append("..")
    sys.path.append(path.dirname(__file__))
    nonebot.init(config)
    # nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins'
    )

    nonebot.run(host='127.0.0.1', port=8080)
