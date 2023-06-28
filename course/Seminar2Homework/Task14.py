# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k ), не превосходящие числа N.
# 10 -> 1 2 4 8

from math import *

n = 1025
print(n, end=" -> ")
for i in range (ceil(log2(n))):
    if 2 ** i < n:
        print(2 ** i, end=" ")

