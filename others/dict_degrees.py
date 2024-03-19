
def change_degrees(degrees_value, how_degrees='cf'):
    dict_of_degrees = {
        'cf': lambda degrees_value: (degrees_value * (9/5)) + 32,
        'fc': lambda degrees_value: ((degrees_value - 32) * 5) / 9,
        'ck': lambda degrees_value: degrees_value + 273.15,
        'kc': lambda degrees_value: degrees_value - 273.15,
        'fk': lambda degrees_value: (((degrees_value - 32) * 5) / 9) - 273.15,
        'kf': lambda degrees_value: (((degrees_value - 32) * 5) / 9) - 273.15
    }
    new_degrees = dict_of_degrees[how_degrees]
    return new_degrees(degrees_value)

print(change_degrees(93.2, 'fc'))
