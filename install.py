import os

os.system('pip install -r requirements.txt')
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
os.system('python setup.py sdist')
os.system('python setup.py install')
