from src.lst_work import *
from src.widget import *


def main(operations):
    user_file = int(input("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла)
"""))

    if user_file == 1:
        print("Для обработки выбран JSON-файл")
    elif user_file == 2:
        print("Для обработки выбран CSV-файл")
    elif user_file == 3:
        print("Для обработки выбран XLSX-файл")
    else:
        print("Некорректный ввод")

    user_state = input("""Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").upper()
    states = ["EXECUTED", "CANCELED", "PENDING"]
    if user_state not in states:
        user_state = input("""Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").upper()
    else:
        print(f'Операции отфильтрованы по статусу "{user_state}"')

    state_filter = []
    for operation in operations:
        if operation["state"] == user_state:
            state_filter.append(operation)

    date_filter = input("Отсортировать операции по дате? Да/Нет ").title()
    if date_filter == 'Да':
        reverse_filter = input("Отсортировать по возрастанию или по убыванию? ").title()
        if reverse_filter == 'Да':
            pass

    rub_filter = input("Выводить только рублевые тразакции? Да/Нет ").title()
    if rub_filter == 'Да':
        rub_filter_func = filter_lst_by_string(state_filter, 'RUB')
    else:
        rub_filter_func = state_filter

    word_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").title()
    if word_filter == 'Да':
        user_word = input("Введите слово: ")
        word_filter_func = filter_lst_by_string(state_filter, user_word)
    else:
        word_filter_func = state_filter

    total_operations = []

    for operation in word_filter_func:
        for dictionary in rub_filter_func:
            if operation == dictionary:
                total_operations.append(operation)

    print("""
Распечатываю итоговый список транзакций...
""")

    if total_operations != []:
        print(f"Всего банковских операций в выборке: {len(total_operations)}")
        print("")

        for i in total_operations:
            description = i["description"]
            print(f"{get_date(i["date"])} {description}")
            if description == "Открытие вклада":
                print(mask_account_card(i["to"]))
            else:
                print(f"{mask_account_card(i["from"])} -> {mask_account_card(i["to"])}")
            print(f"Сумма: {i.get("operationAmount").get("amount")} {i.get("operationAmount").get("currency").get("name")}")
            print("")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
      
