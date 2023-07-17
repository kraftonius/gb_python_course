from database import *
from view import *


def main():
    while True:
        num = int(input_num())
        if num == 0:
            print("Иницирован выход из программы")
            break
        if num == 1:
            name = input_name()
            write_name(name)
            print("Успешно записано\n")
        if num == 2:
            a = input_found()
            a.rstrip()
            print(read_found(a))
        if num == 3:
            sort()
            print("Успешно отсортировано\n")
        if num == 4:
            name = input_delete()
            deleted = delete_name(name)
            print(f"Успешно удалена запись: {deleted}\n")
        if num == 5:
            show_telephones()
            print("-- Все записи выведены --\n")

main()



