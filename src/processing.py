from datetime import datetime


def filter_by_state(lst: list, state: str = "EXECUTED") -> list:
    """возвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    new_lst = []
    try:
        for dictionary in lst:
            for key, value in dictionary.items():
                if key == "state":
                    if value == state:
                        new_lst.append(dictionary)

        return new_lst
    except ValueError:
        return 'Некорректный ввод данных'


def sort_by_date(lst: list, reverse_state: bool = False) -> list:
    """Возвращает новый список словарей,
    отсортированный по дате"""

    def get_date(dictionary: dict) -> datetime:
        """Преобразует строку даты из словаря в объект datetime"""
        return datetime.strptime(dictionary["date"], "%Y-%m-%dT%H:%M:%S.%f")

    new_lst = sorted(lst, key=get_date, reverse=not reverse_state)
    return new_lst
