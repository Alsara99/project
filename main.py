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
      
if __name__ == "__main__":
    main([{
    "id": 619287771,
    "state": "EXECUTED",
    "date": "2019-08-19T16:30:41.967497",
    "operationAmount": {
      "amount": "81150.87",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 17691325653939384901",
    "to": "Счет 49304996510329747621"
  },
  {
    "id": 490100847,
    "state": "EXECUTED",
    "date": "2018-12-22T02:02:49.564873",
    "operationAmount": {
      "amount": "56516.63",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Gold 8326537236216459",
    "to": "MasterCard 6783917276771847"
  },
  {
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2019-05-19T12:51:49.023880",
    "operationAmount": {
      "amount": "6381.58",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "МИР 5211277418228469",
    "to": "Счет 58518872592028002662"
  },
  {
    "id": 27192367,
    "state": "CANCELED",
    "date": "2018-12-24T20:16:18.819037",
    "operationAmount": {
      "amount": "991.49",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 71687416928274675290",
    "to": "Счет 87448526688763159781"
  },
  {
    "id": 921286598,
    "state": "EXECUTED",
    "date": "2018-03-09T23:57:37.537412",
    "operationAmount": {
      "amount": "25780.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 26406253703545413262",
    "to": "Счет 20735820461482021315"
  },
  {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {
      "amount": "92688.46",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 35737585785074382265"
  },
  {
    "id": 957763565,
    "state": "EXECUTED",
    "date": "2019-01-05T00:52:30.108534",
    "operationAmount": {
      "amount": "87941.37",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 46363668439560358409",
    "to": "Счет 18889008294666828266"
  },
  {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }])
