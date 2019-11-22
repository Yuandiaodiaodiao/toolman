import os
if __name__=="__main__":

    if os.name=="nt":
        import env_windows.launcher
        env_windows.launcher.run()
    else:
        import env_linux.launcher
        env_linux.launcher.run('init')
