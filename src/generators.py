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