# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


number = 337913

first_n = f = number // 1000
second_n = s = number % 1000
sum1 = sum2 = 0
while f > 0 or s > 0:
    sum1 += f % 10
    f //= 10
    sum2 += s % 10
    s //= 10
if sum1 == sum2:
    print("yes")
else:
    print("no")
