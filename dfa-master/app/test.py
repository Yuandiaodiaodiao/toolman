from dfa import DFA



def check_sensitive(content):
    filename = "keywords"
    dfa = DFA(filename)
    return dfa.dfa(content)


print(check_sensitive("毒品包括海洛因，冰毒，大麻等，我国禁止AV，三级片，禁止未成年人吸食毒品，涉黄等行为"))