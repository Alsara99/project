import pytest


@pytest.fixture
def card_numbers():
    return [7000792289606361,
            5124364654134534,
            5431236466723452,
            1246335763453455,
            'fwrefwerf']


@pytest.fixture
def accounts():
    return [70007922896063611523,
            51243646541345341563,
            54312364667234527422,
            12463357634534557644,
            'fwrefwerf']


@pytest.fixture
def cards_and_accounts():
    return ['Maestro 1596837868705199',
            'Счет 64686473678894779589',
            'MasterCard 7158300734726758',
            'Счет 35383033474447895560',
            'Visa Classic 6831982476737658',
            'Visa Platinum 8990922113665229',
            'Visa Gold 5999414228426353',
            'Счет 73654108430135874305']


@pytest.fixture
def dates():
    return ['2024-03-11T02:26:18.671407',
            '2000-01-01T00:00:00.000000',
            '1999-12-31T23:59:59.999999',
            'frwefwg']


@pytest.fixture
def list_of_dictionaries():
    return [{'id': 41428829, 'state': 'EXECUTED',
             'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED',
             'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED',
             'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED',
             'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
