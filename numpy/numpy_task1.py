import numpy as np

money = np.array([35800])

percent_matrix = []

procent = "15 8 10;10 11 13;20 7 4"
array_procent = procent.split(';')
for i in array_procent:
    percent_matrix.append(tuple(map(int, i.split(' '))))
percent_matrix = np.array(percent_matrix)

much_greed = [(x := np.max(i)) for i in percent_matrix]
for i in much_greed:
    money = i * (money / 100) + money

print(money)
