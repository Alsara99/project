import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)


def get_mask_card_number(number: int) -> str:
    """Возвращает замаскированный номер карты"""
    card_number = str(number)
    if card_number == '':
        logger.error("Пустой ввод")
        return ''
    elif card_number.isdigit() and len(card_number) == 16:
        groups_of_card_number = [card_number[:4],
                                 card_number[4:6] + "**",
                                 "****",
                                 card_number[-4:]]
        result = ""
        for i in groups_of_card_number:
            result = result + i + " "
        logger.info("Возврат замаскированного номера карты")
        return result[:-1]
    else:
        logger.error("Некорректный ввод данных")
        return 'Некорректный ввод данных'


def get_mask_account(number: int) -> str:
    """Возвращает замаскированный номер счёта"""
    account_number = str(number)
    if account_number == '':
        logger.error("Пустой ввод")
        return ''
    elif account_number.isdigit() and len(account_number) == 20:
        result = "**" + account_number[-4:]
        logger.info("Возврат замаскированного номера счёта")
        return result
    else:
        logger.error("Некорректный ввод данных")
        return 'Некорректный ввод данных'
        
