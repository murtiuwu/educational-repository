def change_degrees(degrees_value, how_degrees='C', new_degrees='F'):
    if how_degrees.lower() == 'c' and new_degrees.lower() == 'f':
        new_degrees_value = (degrees_value * (9/5)) + 32
        return new_degrees_value
    elif how_degrees.lower() == 'f' and new_degrees.lower() == 'c':
        new_degrees_value = ((degrees_value - 32) * 5) / 9
        return new_degrees_value
    elif how_degrees.lower() == 'c' and new_degrees.lower() == 'k':
        new_degrees_value = degrees_value + 273.15
        return new_degrees_value
    elif how_degrees.lower() == 'k' and new_degrees.lower() == 'c':
        new_degrees_value = degrees_value - 273.15
        return new_degrees_value
    elif how_degrees.lower() == 'k' and new_degrees.lower() == 'f':
        degrees_value = ((degrees_value - 32) * 5) / 9
        new_degrees_value = degrees_value - 273.15
        return new_degrees_value
    elif how_degrees.lower() == 'f' and new_degrees.lower() == 'k':
        degrees_value = ((degrees_value - 32) * 5) / 9
        new_degrees_value = degrees_value + 273.15
        return new_degrees_value

print(change_degrees(1, 'f', 'k'))
