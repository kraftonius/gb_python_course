# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def if_fibo_seq_num(a):
    if a <= 1:
        return -1
    fprev = 1
    fnext = 1
    fnew = 0
    count = 4
    while fnew <= a:
        fnew = fprev + fnext
        if fnew == a:
            return count
        if fnew > a:
            return -1
        fprev = fnext
        fnext = fnew
        count += 1

number = 2
print(if_fibo_seq_num(number))
