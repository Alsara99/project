import json

import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../PythonProject/logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)


def get_data(path):
    """принимает на вход путь до JSON-файла и
    возвращает список словарей с данными
     о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if data:
            logger.info("Возврат списка словарей с данными о финансовых транзакциях")
            return data
        else:
            logger.error("Пустой файл")
            return []
    except Exception as e:
        logger.error("Файл не найден")
        return []
