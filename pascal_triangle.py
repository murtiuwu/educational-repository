
import copy

def bricks_dek(func):
    def wrapper(args):

        new_values = func(args)
        for i in range(len(new_values)):
            new_values[i] = new_values[i].split(' ')
        biggest_value = len(str(max(max(new_values))))
        biggest_len = len(max(new_values, key=len))

        for func_values in new_values:
            resultat = []
            roof = ("---" + ("-" * biggest_value)) * len(func_values) + '-'
            print('\n', roof.center(biggest_len * 6), sep='')

            for i in func_values:
                i = str(i)
                resultat.append('|' + i.center(biggest_value+2))
            resultat = ''.join(resultat)
            resultat += '|'
            print(resultat.center(biggest_len * 6), end='')
        print('\n', roof.center(biggest_len * 6), sep='')
    return wrapper

@bricks_dek
def pascal_triangle(floors):
    if floors == 0:
        print(1)
    else:
        list_of_floors = ['1', '1 1']
        while floors != 1:
            last_floor = []
            floors -= 1
            last_floor_values = list_of_floors[-1].split(' ')
            for i in range(len(last_floor_values) - 1):
                last_floor.append(str(int(last_floor_values[i]) + int(last_floor_values[i+1])) + ' ')

            list_of_floors.append('1 ' + ''.join(last_floor) + '1')

        return list_of_floors



# print(pascal_triangle(6))
pascal_triangle(10)
