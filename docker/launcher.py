# -*- coding: <encoding name> -*-
import os
import sys
import shutil
import json

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


def cp():
    try:
        os.mkdir("./coolq/bin")
    except:
        pass
    copyList = ["cqc.exe", "ffmpeg.exe"]
    fromdir = "../env_windows/bin"
    todir = "./coolq/bin"
    for name in copyList:
        shutil.copyfile(os.path.join(fromdir, name), os.path.join(todir, name))
    # shutil.copyfile("../env_windows/bin/libeay32.dll", "./coolq/bin")
    # shutil.copyfile("../env_windows/bin/zlib1.dll", "./coolq/bin")


def accountIn(account):
    try:
        os.makedirs("./coolq/conf")
    except:
        pass
    cqpcfg = f"""
    [App]
        io.github.richardchien.coolqhttpapi.status=1
    [Login]
        Account={account}
    """
    with open("./coolq/conf/CQP.cfg", 'w')as f:
        f.write(cqpcfg)
    cqAccount="""[Account]
    session.2089883591=1
    """
    with open("./coolq/conf/Account.cfg", 'w')as f:
        f.write(cqAccount)
def config(account):
    global jsglobalconfig
    configdir = "./coolq/data/app/io.github.richardchien.coolqhttpapi/config"
    try:
        os.makedirs("./coolq/data/app/io.github.richardchien.coolqhttpapi/config")
    except:
        pass
    serverip = "ip.oops-sdu.cn"
    serverport = "9002"
    jsglobalconfig["ws_reverse_api_url"] = f"ws://{serverip}:{serverport}/ws/api/"
    jsglobalconfig["ws_reverse_event_url"] = f"ws://{serverip}:{serverport}/ws/event/"
    with open(os.path.join(configdir, f"{account}.json"), 'w')as f:
        f.write(json.dumps(jsglobalconfig, indent=4))


if __name__ == "__main__":
    op = sys.argv[1]
    qqid = 2089883591
    if op == "init":
        try:
            os.mkdir("./coolq")
        except:
            pass
        os.system("docker-compose up -d --no-recreate")
        cp()
        accountIn(qqid)
        config(qqid)
    if op == "ps":
        os.system("docker-compose ps")
    if op == "cp":
        cp()
    if op == "start":
        os.system("docker-compose up -d --no-recreate")
    if op == "ps":
        os.system("docker-compose ps")
    if op == "stop":
        os.system("docker stop coolqbot")
    if op == "rm":
        os.system("docker stop coolqbot")
        os.system("docker rm coolqbot")
