# -*- coding: <encoding name> -*-
import os
import sys
import shutil
import json

PATH_THIS_FLODER = os.path.dirname(os.path.abspath(__file__))

try:
    from myConfig.configJson import configJs
except:
    try:
        toolmandir = os.path.dirname(os.path.dirname(__file__))
        sys.path.append(toolmandir)
        from myConfig.configJson import configJs
    except:
        print('configJs error')
jsglobalconfig = {
    "use_http": False,
    "use_ws": False,
    "ws_reverse_url": "",
    "ws_reverse_api_url": "ws://127.0.0.1:8080/ws/api/",
    "ws_reverse_event_url": "ws://127.0.0.1:8080/ws/event/",
    "ws_reverse_reconnect_interval": 3000,
    "ws_reverse_reconnect_on_code_1000": True,
    "use_ws_reverse": True,
    "show_log_console": False,
    "enable_rate_limited_actions": False,
    "rate_limit_interval": 100,
    "thread_pool_size": 0,
    "server_thread_pool_size": 0,
}


def accountIn(account):
    try:
        os.makedirs(os.path.join(PATH_THIS_FLODER, "./conf"))
    except:
        pass
    cqpcfg = f"""
      [App]
          io.github.richardchien.coolqhttpapi.status=1
      [Login]
          Account={account}
      """
    with open(os.path.join(PATH_THIS_FLODER, "./conf/CQP.cfg"), 'w')as f:
        f.write(cqpcfg)
    with open(os.path.join(PATH_THIS_FLODER, "./conf/CQA.cfg"), 'w')as f:
        f.write(cqpcfg)

    cqAccount = f"""[Account]
      session.{account}=1
      """
    with open(os.path.join(PATH_THIS_FLODER, "./conf/Account.cfg"), 'w')as f:
        f.write(cqAccount)


def config(account):
    global jsglobalconfig
    configdir = os.path.join(PATH_THIS_FLODER, "./data/app/io.github.richardchien.coolqhttpapi/config")
    try:
        os.makedirs(configdir)
    except:
        pass
    serverip = configJs["serverip"]
    serverport = configJs["nonebotListen"]
    jsglobalconfig["ws_reverse_api_url"] = f"ws://{serverip}:{serverport}/ws/api/"
    jsglobalconfig["ws_reverse_event_url"] = f"ws://{serverip}:{serverport}/ws/event/"
    with open(os.path.join(configdir, f"{account}.json"), 'w')as f:
        f.write(json.dumps(jsglobalconfig, indent=4))


def run():
    qqid = configJs["qq_id"]
    accountIn(qqid)
    config(qqid)


if __name__ == "__main__":
    run()
