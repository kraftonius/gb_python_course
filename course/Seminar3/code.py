# lst = []
# for i in range(1, 30 + 1):
#     lst.append(i)
#
# print(lst)
#
# a = [i if i % 2 == 0 else v for i in range(4) for v in range(4)]
#
# print(a)
#
# dct = {i:1 for i in range(1,10)}
# print(dct)


# import time
# a = [i for i in range(150000)]
# start = time.perf_counter()
# if 130000 in a:
#     print("нашел в списке")
# end = time.perf_counter()
# print(end - start)


# dct = {i:1 for i in range(150000)}
# start = time.perf_counter()
# if 130000 in dct:
#     print("нашел в словаре")
# end = time.perf_counter()
# print(end - start)

a = set()
a.add(2)
a.add(3)
a.add("t")
a.add("4")
print(a)