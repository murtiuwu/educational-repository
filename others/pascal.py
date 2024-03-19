dict_of_variable = {}

def readln(in_put):
    dict_of_variable[in_put] = input()
    return dict_of_variable

readln('my word')

print(dict_of_variable['my word'])