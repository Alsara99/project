from typing import Any

from masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> Any:
    """
    обрабатывает информацию о картах/счетах и выводит их замаскированную версию
    """

    if "Счет" in string:
        return get_mask_account(int(string[-20:]))
    else:
        return get_mask_card_number(int(string[-16:]))


def get_date(date: str) -> str:
    result = date[8:10] + "." + date[5:7] + "." + date[:4]
    return result
