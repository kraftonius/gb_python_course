# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint


n = int(input("Введите размер массива A[1..N]: "))
arr_x = [randint(1, n) for i in range(1, n + 1)]
arr_x.sort()
print(arr_x)
x = int(input(f"Введите натуральное число для поиска самого близкого по величине: "))
if x <= 0:
    print(f"введено не натуральное число {x}")
else:
    list_x = [abs(x - i) for i in arr_x]
    min_delta = list_x[0]
    ind = 0
    for index, value in enumerate(list_x):
        if value < min_delta:
            min_delta = value
            ind = index
    print(arr_x[ind])
