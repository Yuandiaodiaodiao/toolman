from dfa import DFA



def check_sensitive(content):
    filename = "keywords"
    dfa = DFA(filename)
    return dfa.dfa(content)


print(check_sensitive("123!4124123TMD3124125123"))