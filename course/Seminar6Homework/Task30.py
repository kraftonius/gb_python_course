# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def get_next_number(a, d, n):
    return a + (n - 1) * d


def get_progression(a, d, n):
    arr = []
    for i in range(1, qty + 1):
        arr.append(get_next_number(a1, d_multiplier, i))
    return arr


a1 = int(input("Введите число - первый элемент арифметической прогрессии: "))
d_multiplier = int(input("Введите число - разность арифметической прогрессии: "))
qty = int(input("Введите число - количество элементов арифметической прогрессии: "))
print(get_progression(a1, d_multiplier, qty))
