# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def gen_list(n):
    element_list = []
    for i in range(n):
        element_list.append(randint(1, 100))
    return element_list


def get_indexes(lst, start, finish):
    indexes_list = []
    for i in range(len(lst)):
        if start <= lst[i] <= finish:
            indexes_list.append(i)
    return indexes_list


min_el_search = 5
max_el_search = 25
list_len = 15
my_el_list = gen_list(list_len)
my_index_list = get_indexes(my_el_list, min_el_search, max_el_search)
print(my_el_list)
print(my_index_list)
