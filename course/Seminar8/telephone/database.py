def write_name(name):
    with open("tel.txt", "r") as file:
        lst = file.readlines()
    with open("tel.txt", "a") as file:
        if len(lst) == 0:
            file.write(f"{name}")
        else:
            file.write(f"\n{name}")


def read_found(a):
    with open("tel.txt", "r") as file:
        lst = file.readlines()
        for i in lst:
            if a.lower() in i.lower():
                print(i)


def sort():
    with open("tel.txt", "r") as file:
        lst = file.readlines()
        lst = [line.rstrip() for line in lst]
        lst.sort()
    with open("tel.txt", "w+") as file:
        file.readlines()
    with open("tel.txt", "a") as file:
        for i in lst:
            write_name(i)


def delete_name(name):
    with open("tel.txt", "r") as file:
        lst = file.readlines()
        lst = [line.rstrip() for line in lst]
        new_lst = list(enumerate(lst))
        for i in range(len(new_lst)):
            if name.lower() in new_lst[i][1].lower():
                print(f"{new_lst[i][0] + 1} --> {new_lst[i][1]}")
        input_text = "Для удаления введите номер записи для удаления\nДля отмены введите 0\n"
        del_line = int(input(input_text))
        if del_line == 0:
            print("Удаление отменено")
        else:
            with open('tel.txt', 'w') as file:
                for i in range(len(new_lst)):
                    if del_line - 1 != new_lst[i][0]:
                        if i == 0:
                            file.write(new_lst[i][1])
                        else:
                            file.write(f"\n{new_lst[i][1]}")
                    else:
                        deleted = new_lst[i][1]
    return deleted


def show_telephones():
    with open("tel.txt", "r") as file:
        lst = file.readlines()
        lst = [line.rstrip() for line in lst]
        new_lst = list(enumerate(lst))
    print("Телефонная книга:")
    for i in range(len(new_lst)):
        print(f"{new_lst[i][0]} --> {new_lst[i][1]}")
