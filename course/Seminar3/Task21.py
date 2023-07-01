# Напишите программу для печати всех уникальных значений в словаре.
#
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
#
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
#
# Примечание: Список словарей задан изначально. Пользователь его не вводит

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
           {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
my_set = set()
for d in my_list:
    for c in d.values():
        my_set.add(c)
        print(c)
print(my_set)

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
           {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print(set().union(*(d.values() for d in my_list)))

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#           {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
#
# set_n = set()
#
# for dct in list_1:
#     set_n.add(str(*dct.values()).strip())
#
# print(set_n)