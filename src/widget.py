from typing import Any

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> Any:
    """
    обрабатывает информацию о картах/счетах
    выводит их замаскированную версию
    """
    try:
        if string == '':
            return ''
        elif "Счет" in string:
            return f'Счет {get_mask_account(int(string[-20:]))}'
        else:
            return f'{string[:-16]}{get_mask_card_number(int(string[-16:]))}'
    except ValueError:
        return 'Некорректный ввод данных'


def get_date(date: str) -> str:
    try:
        if date == '':
            return ''
        result = date[8:10] + "." + date[5:7] + "." + date[0:4]
        return result
    except ValueError:
        return 'Некорректный ввод данных'
