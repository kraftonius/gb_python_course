# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.

a = 7
b = 12
c = 7
my_list = [a, b, c]
my_list.sort()
if my_list[0] + my_list[1] > my_list[2]:
    print("YES")
else:
    print("NO")