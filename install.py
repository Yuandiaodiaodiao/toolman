import os
import sys
if __name__=="__main__":
    pythonstr=sys.argv[1]
    pipstr=sys.argv[2]
    if len(pipstr)==0:
        pipstr="pip"
    if len(pythonstr)==0:
        pythonstr="python"
    os.system(f"{pipstr}   install -r requirements.txt")
    try:
        os.mkdir('./install')
    except:
        pass
    try:
        os.mkdir('./install/Abstract_Words')
    except:
        pass
    os.system('git clone https://github.com/yhm12345/Abstract_Words.git ./install/Abstract_Words')
    os.chdir('./install/Abstract_Words')
    os.system(f'{pythonstr} setup.py sdist')
    os.system(f'{pythonstr} setup.py install')
