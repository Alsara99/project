import pytest

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


@pytest.mark.parametrize("start, end, expected_result", [
    (1, 1, ["0000 0000 0000 0001"]),
    (50, 52, ["0000 0000 0000 0050", "0000 0000 0000 0051", "0000 0000 0000 0052"]),
    (5649175983145137, 5649175983145139, [
        "5649 1759 8314 5137",
        "5649 1759 8314 5138",
        "5649 1759 8314 5139"
    ])
])
def test_card_number_generator(start, end, expected_result):
    assert list(card_number_generator(start, end)) == expected_result