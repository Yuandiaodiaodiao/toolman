from multiprocessing import Process
import botCore.botServer
import botCore.messageServer
import rss_fetch.main
import messages.messages_server

if __name__ == "__main__":
    processList = []
    processList.append(Process(target=botCore.botServer.run, name="botCore.botServer"))
    processList.append(Process(target=botCore.messageServer.run, name="botCore.messageServer"))
    processList.append(Process(target=rss_fetch.main.run, name="rss_fetch.main"))
    processList.append(Process(target=messages.messages_server.run, name="messages.messages_server"))
    for i in processList:
        i.start()
    while True:
        for i in processList:
            if not i.is_alive():
                i.run()
            else:
                pass
                # print(f"process {i.pid} {i.name} {i.} ")
