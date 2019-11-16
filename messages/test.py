import json
import os

a = os.listdir('images/have_name')
bqb = {}
for item in os.listdir('images/have_name'):
    name = item.split('.')[0]
    bqb[name] = 'images/have_name/' + item
print(bqb)
