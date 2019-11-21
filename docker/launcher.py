# -*- coding: <encoding name> -*-
import os
import sys
import shutil
def cp():
    try:
        os.mkdir("./coolq/bin")
    except:
        pass
    copyList=["cqc.exe","ffmpeg.exe"]
    fromdir="../botexe/bin"
    todir="./coolq/bin"
    for name in copyList:
        shutil.copyfile(os.path.join(fromdir,name),os.path.join(todir,name))
    # shutil.copyfile("../botexe/bin/libeay32.dll", "./coolq/bin")
    # shutil.copyfile("../botexe/bin/zlib1.dll", "./coolq/bin")

if __name__ == "__main__":
    op = sys.argv[1]
    if op == "init":
        try:
            os.mkdir("./coolq")
        except:
            pass
        os.system("docker-compose up -d --no-recreate")
        cp()
    if op == "ps":
        os.system("docker-compose ps")
    if op == "cp":
       cp()
    if op == "start":
        os.system("docker-compose up -d --no-recreate")
    if op == "ps":
        os.system("docker-compose ps")
