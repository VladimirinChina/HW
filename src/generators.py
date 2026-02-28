from typing import Iterator, Dict, Any, List


def filter_by_currency(
    transactions: List[Dict[str, Any]],
    currency_code: str
) -> Iterator[Dict[str, Any]]:
    """
    Generator that filters transactions by currency code.

    :param transactions: List of transaction dictionaries
    :param currency_code: Currency code (e.g. "USD")
    :return: Iterator of filtered transactions
    """
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code") == currency_code
        ):
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Iterator[str]:
    """
    Generator that yields transaction descriptions.

    :param transactions: List of transaction dictionaries
    :return: Iterator of descriptions
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Generator that yields card numbers in format XXXX XXXX XXXX XXXX.

    :param start: start number (inclusive)
    :param stop: stop number (inclusive)
    :return: iterator of formatted card numbers
    """
    for number in range(start, stop + 1):
        # превращаем число в строку длиной 16 символов с ведущими нулями
        card_number = f"{number:016d}"

        # разбиваем на группы по 4
        formatted = (
            f"{card_number[0:4]} "
            f"{card_number[4:8]} "
            f"{card_number[8:12]} "
            f"{card_number[12:16]}"
        )

        yield formatted
