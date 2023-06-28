# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа
# 4 4 -> 2 2
# 5 6 -> 2 3

from math import sqrt

# Петя
x = 7
y = 11
s = x + y
p = x * y
print(s, p, end=" -> ")

# Катя
# y = s - x
# p = x * (s - x)
# p = x*s - x^2
# x^2 - s * x + p = 0 --> a = 1, b = -s, c = p

a = 1
b = -s
c = p
nx = ny = 0
x1 = 0
x2 = 0
discriminant = b * b - 4 * a * c
if discriminant > 0:
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
elif discriminant == 0:
    x1 = -b / (2 * a)
else:
    nx = ny = 0
if x1 > 0 or x2 > 0:
    nx = int(max(x1, x2))
    ny = s - nx
    (nx, ny) = tuple(sorted((nx, ny)))

print(nx, ny)
