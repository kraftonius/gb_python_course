# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


from random import randint


def create_list(n):
    i = 1
    new_list = []
    while i <= n:
        new_list.append(randint(1, 12))
        i += 1
    return new_list


def get_same_numbers(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    set3 = set1.intersection(set2)
    return sorted(list(set3))


list_len1 = int(input("Введите количество элементов 1-ого списка: "))
list_len2 = int(input("Введите количество элементов 2-ого списка: "))

list1 = create_list(list_len1)
list2 = create_list(list_len2)

print(list1)
print(list2)
print(get_same_numbers(list1, list2))


