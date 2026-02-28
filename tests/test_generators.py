from typing import Any, Iterator

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)

def test_filter_by_currency_usd(transactions_fixture: list[dict[str, Any]]) -> None:
    generator: Iterator[dict[str, Any]] = filter_by_currency(transactions_fixture, "USD")

    results = list(generator)

    assert len(results) == 3

    for transaction in results:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"

def test_filter_by_currency_empty(transactions_fixture: list[dict[str, Any]]) -> None:
    generator = filter_by_currency(transactions_fixture, "EUR")

    results = list(generator)

    assert results == []

def test_transaction_descriptions(transactions_fixture: list[dict[str, Any]]) -> None:
    generator = transaction_descriptions(transactions_fixture)

    results = list(generator)

    assert results == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

def test_card_number_generator() -> None:
    generator = card_number_generator(1, 3)

    results = list(generator)

    assert results == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (9999, 10000, [
            "0000 0000 0000 9999",
            "0000 0000 0001 0000",
        ]),
    ],
)
def test_card_number_generator_parametrized(
    start: int,
    stop: int,
    expected: list[str],
) -> None:
    result = list(card_number_generator(start, stop))

    assert result == expected
