from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions):
    test = list(filter_by_currency(transactions, "RUB"))
    assert len(test) == 2
    assert all(i["operationAmount"]["currency"]["code"] == "RUB" for i in test)


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Перевод организации",
"Перевод со счета на счет",
"Перевод со счета на счет",
"Перевод с карты на карту",
"Перевод организации"]


def test_card_number_generator():
    test = list(card_number_generator(1,5))
    assert test == ["0000 0000 0000 0001",
"0000 0000 0000 0002",
"0000 0000 0000 0003",
"0000 0000 0000 0004",
"0000 0000 0000 0005"]
