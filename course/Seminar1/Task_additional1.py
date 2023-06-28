# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца
# и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES,
# если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
# В случае, если хотя бы одно из введенных чисел не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".


my_list = [0] * 4

for i in range(4):
    my_list[i] = int(input(f"введите номер {i + 1}-й координаты: "))
    if not 1 <= my_list[i] <= 8:
        print("Такой клетки на доске нет!")
        break

if (abs(my_list[0] - my_list[2]) <= 1 and abs(my_list[1] - my_list[3]) <= 1) and \
        (my_list[0] != 0 and my_list[1] != 0 and my_list[2] != 0 and my_list[3]):
    print("YES")
else:
    print("NO")