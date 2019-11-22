# -*- coding: <encoding name> -*-
import os
import sys
import shutil
import json

jsglobalconfig = {
    "use_http": False,
    "use_ws": False,
    "ws_reverse_api_url": "ws://127.0.0.1:8080/ws/api/",
    "ws_reverse_event_url": "ws://127.0.0.1:8080/ws/event/",
    "use_ws_reverse": True,
    "show_log_console": False,
}


def accountIn(account):
    try:
        os.makedirs("./conf")
    except:
        pass
    cqpcfg = f"""
    [App]
        io.github.richardchien.coolqhttpapi.status=1
    [Login]
        Account={account}
    """
    with open("./conf/CQP.cfg", 'w')as f:
        f.write(cqpcfg)
    cqAccount = f"""[Account]
    session.{account}=1
    """
    with open("./conf/Account.cfg", 'w')as f:
        f.write(cqAccount)


def config(account):
    global jsglobalconfig
    configdir = "./data/app/io.github.richardchien.coolqhttpapi/config"
    try:
        os.makedirs(configdir)
    except:
        pass
    serverip = "127.0.0.1"
    serverport = "9002"
    jsglobalconfig["ws_reverse_api_url"] = f"ws://{serverip}:{serverport}/ws/api/"
    jsglobalconfig["ws_reverse_event_url"] = f"ws://{serverip}:{serverport}/ws/event/"
    with open(os.path.join(configdir, f"{account}.json"), 'w')as f:
        f.write(json.dumps(jsglobalconfig, indent=4))


if __name__ == "__main__":
    PATH_THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    qqid = 1442766687
    accountIn(qqid)
    config(qqid)
