def input_num():
    ask = int(input("""Выбери действие:
    0 - Выйти из программы
    1 - Показать всю телефонную книгу
    2 - Поик по характеристике  
    3 - Записать нового пользователя
    4 - Сортировка списка
    5 - Изменить Запись
    6 - Удалить запись
    """))
    return ask


def input_name():
    name = input("Введите данные: \n")
    return name


def input_found():
    found = input("Введите параметр для поиска: \n")
    return found

def input_change():
    name = input("Введите Имя, Фамилию или Номер для изменения (можно частично): \n")
    return name

def input_delete():
    name = input("Введите Имя, Фамилию или Номер для удаления (можно частично): \n")
    return name
