def how_change_degrees(how_degrees):
    def change_degrees(degrees_value):
        dict_of_degrees = {
            'cf': lambda degrees_value: (degrees_value * (9 / 5)) + 32,
            'fc': lambda degrees_value: ((degrees_value - 32) * 5) / 9,
            'ck': lambda degrees_value: degrees_value + 273.15,
            'kc': lambda degrees_value: degrees_value - 273.15,
            'fk': lambda degrees_value: (((degrees_value - 32) * 5) / 9) - 273.15,
            'kf': lambda degrees_value: (((degrees_value - 32) * 5) / 9) - 273.15
        }
        new_degrees = dict_of_degrees[how_degrees]
        return new_degrees(degrees_value)
    return change_degrees



celsius_to_fahrenheit = how_change_degrees("cf")
print(celsius_to_fahrenheit(25))