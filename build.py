import os
from myConfig.configJson import configJs
if __name__=="__main__":

    if os.name=="nt":
        import env_windows.launcher
        env_windows.launcher.run()
        if configJs["isPro"]:
            os.system('./env_windows/CQP.exe')
        else:
            os.system('./env_windows/CQA.exe')
    else:
        import env_linux.launcher
        env_linux.launcher.run('init')
