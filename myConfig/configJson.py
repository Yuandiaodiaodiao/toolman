import json
import os
import json5
import shutil
PATH_THIS_FLODER = os.path.dirname(os.path.abspath(__file__))
PATH_CONFIG = os.path.join(PATH_THIS_FLODER, 'config.json')
if not os.path.exists(PATH_CONFIG):
    shutil.copyfile( os.path.join(PATH_THIS_FLODER, 'config.json.example'),PATH_CONFIG)
with open(PATH_CONFIG, 'r',encoding='utf-8')as f:
    configJs = json5.load(f)
