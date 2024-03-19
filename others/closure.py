def changeable_list(func):
    list_of_results = []
    def add_values(values=None):
        if values != None:
            list_of_results.append(func(values))
        return list_of_results
    return add_values

squares = changeable_list(lambda x: x ** 2)

for i in range(1, 8):
    squares(i)

print(squares())
