# Домашняя работа 10.1

## Описание:

Мой проект ялвяется виджетомом банковских операций клиента. 

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import transactions

# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

# Пример использования transaction_descriptions
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

# Пример использования card_number_generator
for card_number in card_number_generator(1, 5):
    print(card_number)
```

## Тестирование

В нашем проекте используется тестирование для обеспечения надёжности и корректности работы. Был использован фреймвор pytest.
Все написанные тесты находятся в папке tests, там же можно найти файл со всеми фикстурами в модуле "conftest.py"

```
File	        statements  missing  excluded   coverage
src\__init__.py	    0	        0       0         100%
src\generators.py   9           0       0         100%
src\masks.py	    19	        0       0         100%
src\processing.py   17	        2       0         88%
src\widget.py	    20	        2       0         90%
Total	            65	        4       0         94%