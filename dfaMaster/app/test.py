from .dfa import DFA
filename = "../dfaMaster/app/keywords"
dfa = DFA(filename)
def check_sensitive(content):

    return dfa.dfa(content)[0]


# print(check_sensitive("毒品包括海洛因，冰毒，大麻等，我国禁止AV，三级片，禁止未成年人吸食毒品，涉黄等行为"))