import os
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        pythonstr = sys.argv[1]
    else:
        pythonstr = "python"
    if len(sys.argv) >= 3:
        pipstr = sys.argv[2]
    else:
        pipstr = "pip"
    os.system(f"{pipstr}   install -r requirements.txt")
    os.system(f"""{pipstr}   install "nonebot[scheduler]" """)

    # install ab
    try:
        import ab
    except ImportError:
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
