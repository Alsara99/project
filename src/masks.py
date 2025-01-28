def get_mask_card_number(number: int) -> str:
    """Возвращает замаскированный номер карты"""
    card_number = str(number)
    groups_of_card_number = [card_number[:4], card_number[4:6] + "**", "****", card_number[-4:]]
    result = ""
    for i in groups_of_card_number:
        result = result + i + " "
    return result


def get_mask_account(number: int) -> str:
    """Возвращает замаскированный номер счёта"""
    account_number = str(number)
    result = "**" + account_number[-4:]
    return result
