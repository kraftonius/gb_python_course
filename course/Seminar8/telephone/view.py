def input_num():
    ask = int(input("""Выбери действие:
    0 - Выйти из программы
    1 - Записать нового пользователя
    2 - Поик по характеристике
    3 - Сортировка списка
    4 - Удалить запись
    5 - Показать всю телефонную книгу
    """))
    return ask


def input_name():
    name = input("Введите данные: \n")
    return name


def input_found():
    found = input("Введите параметр для поиска: \n")
    return found


def input_delete():
    name = input("Введите Имя, Фамилию или Номер для удаления (можно частично): \n")
    return name
