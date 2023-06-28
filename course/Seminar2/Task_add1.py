# 3.Даны целые положительные числа A и B.
# Найти их наибольший общий делитель (НОД),
# и наименьшее общее кратное (НОК)

a = 8
b = 16
nod = 0
nok = 0

for i in range(2, min(a, b)):
    if a % i == 0 and b % i == 0:
        nod = i

for i in range (min(a,b), a * b + 1):
    if i % a == 0 and i % b == 0:
        nok = i
        break

print(f"НОД = {nod}")
print(f"НОК = {nok}")