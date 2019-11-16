import json
import requests

data = {
    'qq_group_id': '967636480',
    'qq_id_list':['295087430','1479389468'],
    'text':'n🐎$l',
    'img':''
}
res = requests.post('http://127.0.0.1:50382', data=json.dumps(data))