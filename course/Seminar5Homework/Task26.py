# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def recursive_power(n1, n2):
    if n2 == 1: return n1
    return n1 * recursive_power(n1, n2 - 1)


num1 = 2
num2 = 10
print(f"A = {num1}; B = {num2} -> {recursive_power(num1, num2)}")
