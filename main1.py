"""
Написать функцию для перевода доллара в евро c округлением
до 2х знаков после запятой, если известно, что текущий курс
составляет 1.17 долларов за один евро.

"""


def currency_exchange(usd):
    euro = usd / 1.17
    return euro
euro = currency_exchange(1)

print(round(euro, 2))






