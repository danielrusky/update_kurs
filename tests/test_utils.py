from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 4


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364",
                                         "2019-04-04T23:20:05.206878", "2018-09-12T21:27:25.241689"]


def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
                    '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD',
                    '04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188'
                    '\n79114.93 USD',
                    '23.03.2018 Открытие вклада\nСчет **2431\n48223.05 руб.',
                    '12.09.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657\n67314.70 руб.']
