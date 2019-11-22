# -*- coding: <encoding name> -*-
import os
import sys
import shutil
import json
import yaml

PATH_THIS_FLODER = os.path.dirname(os.path.abspath(__file__))

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
        os.mkdir(os.path.join(PATH_THIS_FLODER, "./coolq/bin"))
    except:
        pass
    copyList = ["cqc.exe", "ffmpeg.exe", "libeay32.dll", "zlib1.dll"]
    fromdir = os.path.join(PATH_THIS_FLODER, "../env_windows/bin")
    todir = os.path.join(PATH_THIS_FLODER, "./coolq/bin")
    for name in copyList:
        shutil.copyfile(os.path.join(fromdir, name), os.path.join(todir, name))
    # shutil.copyfile("../env_windows/bin/libeay32.dll", "./coolq/bin")
    # shutil.copyfile("../env_windows/bin/zlib1.dll", "./coolq/bin")


def accountIn(account):
    try:
        os.makedirs(os.path.join(PATH_THIS_FLODER, "./coolq/conf"))
    except:
        pass
    cqpcfg = f"""
    [App]
        io.github.richardchien.coolqhttpapi.status=1
    [Login]
        Account={account}
    """
    with open(os.path.join(PATH_THIS_FLODER, "./coolq/conf/CQP.cfg"), 'w')as f:
        f.write(cqpcfg)
    with open(os.path.join(PATH_THIS_FLODER, "./coolq/conf/CQA.cfg"), 'w')as f:
        f.write(cqpcfg)

    cqAccount = f"""[Account]
      session.{account}=1
      """
    with open(os.path.join(PATH_THIS_FLODER, "./coolq/conf/Account.cfg"), 'w')as f:
        f.write(cqAccount)


def config(account):
    global jsglobalconfig
    configdir = os.path.join(PATH_THIS_FLODER, "./coolq/app/io.github.richardchien.coolqhttpapi/config")
    try:
        os.makedirs(configdir)
    except:
        pass
    serverip = "host.docker.internal"
    serverport = "9002"
    jsglobalconfig["ws_reverse_api_url"] = f"ws://{serverip}:{serverport}/ws/api/"
    jsglobalconfig["ws_reverse_event_url"] = f"ws://{serverip}:{serverport}/ws/event/"
    with open(os.path.join(configdir, f"{account}.json"), 'w')as f:
        f.write(json.dumps(jsglobalconfig, indent=4))


try:
    from myConfig.configJson import configJs
except:
    try:
        toolmandir = os.path.dirname(os.path.dirname(__file__))
        sys.path.append(toolmandir)
        from myConfig.configJson import configJs
    except:
        print('configJs error')


def run(op):
    qqid = configJs["qq_id"]
    if op == "init":
        pathYml = os.path.join(PATH_THIS_FLODER, "docker-compose.yml")
        with open(pathYml, 'r')as f:
            yml = yaml.load(f)

        if configJs["isPro"]:
            coolq_url = configJs["Pro_url"]
        else:
            coolq_url = configJs["AIR_url"]

        yml['services']['coolqbot']['environment'] = [f'VNC_PASSWD={configJs["VNC_PASSWD"]}', f'COOLQ_URL={coolq_url}',
                                                      'CQHTTP_USE_WS_REVERSE=yes',
                                                      f'CQHTTP_WS_REVERSE_API_URL=ws://172.17.0.1:{configJs["nonebotListen"]}/ws/api/',
                                                      f'CQHTTP_WS_REVERSE_EVENT_URL=ws://172.17.0.1:{configJs["nonebotListen"]}/ws/event/',
                                                      'CQHTTP_SHOW_LOG_CONSOLE=no', 'CQHTTP_USE_HTTP=no',
                                                      'CQHTTP_USE_WS=no']
        yml['services']['coolqbot']['ports'] = [f'{configJs["coolqVNC"]}:9000']
        with open(pathYml, 'w')as f:
            yaml.dump(yml, f)
        try:
            os.mkdir(os.path.join(PATH_THIS_FLODER, "./coolq"))
        except:
            pass
        os.chdir(PATH_THIS_FLODER)
        os.system("docker-compose up -d --no-recreate")
        cp()
        accountIn(qqid)
        # config(qqid)

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
        os.system("docker-compose rm -s -f")
    if op == "clear":
        os.system("rm -rf ./coolq")

if __name__ == "__main__":
    try:
        op = sys.argv[1]
    except:
        op = "init"
    run(op)
