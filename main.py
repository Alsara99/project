import json

from src.lst_work import *
from src.widget import *
from src.file_helper import *
from src.utils import *


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    data = []
    while True:
        user_file = input("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла)
""")
        if user_file == '1':
            print("Для обработки выбран JSON-файл")
            data = get_data("../PythonProject/data/operations.json")
            break
        elif user_file == '2':
            print("Для обработки выбран CSV-файл")
            data = read_csv_file("../PythonProject/data/transactions.csv")
            break
        elif user_file == '3':
            print("Для обработки выбран XLSX-файл")
            data = read_excel_file("../PythonProject/data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный ввод")


    while True:
        user_state = input("""
Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").upper()
        states = ["EXECUTED", "CANCELED", "PENDING"]
        if user_state not in states:
            user_state = input("""Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").upper()
        else:
            print(f'Операции отфильтрованы по статусу "{user_state}"')
            break
    # print(data)
    state_filter = []
    for operation in data:
        if operation.get("state") == user_state:
            state_filter.append(operation)


    date_filter = input("Отсортировать операции по дате? Да/Нет ").title()
    if date_filter == 'Да':
        reverse_filter = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if user_file == '1':
            if reverse_filter == 'по возрастанию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%S.%f"))
            elif reverse_filter == 'по убыванию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
        if user_file == '2' or user_file == '3':
            if reverse_filter == 'по возрастанию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%SZ"))
            elif reverse_filter == 'по убыванию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%SZ"), reverse=True)
        state_filter = date_filter


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

    # print(total_operations)

    if total_operations != []:
        print(f"Всего банковских операций в выборке: {len(total_operations)}")
        print("")

        for i in total_operations:
            description = i.get("description")
            print(f"{get_date(i.get("date"))} {description}")
            if description == "Открытие вклада":
                print(mask_account_card(i.get("to")))
            else:
                print(f"{mask_account_card(i.get("from"))} -> {mask_account_card(i.get("to"))}")
            if user_file == "1":
                print(f"Сумма: {i.get("operationAmount").get("amount")} {i.get("operationAmount").get("currency").get("name")}")
            elif user_file == "2" or user_file == '3':
                # print(data)
                print(f"Сумма: {i.get("amount")} {i.get("currency_code")}")
            print("")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == "__main__":
    main()