from .app.dfa import DFA
import os

filename =os.path.join( os.path.split(os.path.realpath(__file__))[0],"keywords")
dfat = DFA(filename)

def check_sensitive(content):

    return dfat.dfa(content)[0]


# print(check_sensitive("毒品包括海洛因，冰毒，大麻等，我国禁止AV，三级片，禁止未成年人吸食毒品，涉黄等行为"))
