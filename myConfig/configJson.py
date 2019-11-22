import json
import os
import json5
PATH_THIS_FLODER = os.path.dirname(os.path.abspath(__file__))
PATH_CONFIG = os.path.join(PATH_THIS_FLODER, 'config.json')
with open(PATH_CONFIG, 'r')as f:
    configJs = json5.load(f)
