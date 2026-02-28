from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который фильтрует список транзакций по указанному коду валюты.

    :param transactions: Список словарей с информацией о транзакциях
    :param currency_code: Код валюты для фильтрации (например, "USD")
    :return: Итератор с транзакциями, соответствующими указанному коду валюты
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который возвращает описание транзакций.

    :param transactions: Список словарей с информацией о транзакциях
    :return: Итератор со строками описаний транзакций
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, который возвращает номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Номера генерируются последовательно в диапазоне от start до stop включительно.
    Недостающие разряды дополняются ведущими нулями.

    :param start: Начальное число диапазона (включительно)
    :param stop: Конечное число диапазона (включительно)
    :return: Итератор со строками номеров карт в отформатированном виде
    """
    for number in range(start, stop + 1):
        # превращаем число в строку длиной 16 символов с ведущими нулями
        card_number = f"{number:016d}"

        # разбиваем на группы по 4
        formatted = f"{card_number[0:4]} " f"{card_number[4:8]} " f"{card_number[8:12]} " f"{card_number[12:16]}"

        yield formatted
