from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_numbers):
    assert get_mask_card_number(card_numbers[0]) == '7000 79** **** 6361'
    assert get_mask_card_number(card_numbers[1]) == '5124 36** **** 4534'
    assert get_mask_card_number(card_numbers[2]) == '5431 23** **** 3452'
    assert get_mask_card_number(card_numbers[3]) == '1246 33** **** 3455'
    assert get_mask_card_number(card_numbers[4]) == 'Некорректный ввод данных'


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == ''


def test_get_mask_account(accounts):
    assert get_mask_account(accounts[0]) == '**1523'
    assert get_mask_account(accounts[1]) == '**1563'
    assert get_mask_account(accounts[2]) == '**7422'
    assert get_mask_account(accounts[3]) == '**7644'
    assert get_mask_account(accounts[4]) == 'Некорректный ввод данных'


def test_get_mask_account_empty():
    assert get_mask_account('') == ''
