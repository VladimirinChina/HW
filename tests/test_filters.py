from __future__ import annotations

from typing import Any

from src.filters import process_bank_operations, process_bank_search


def test_process_bank_search_found() -> None:
    data = [
        {"description": "Перевод на карту"},
        {"description": "Оплата услуг"},
    ]

    result = process_bank_search(data, "перевод")

    assert len(result) == 1
    assert result[0]["description"] == "Перевод на карту"


def test_process_bank_search_empty() -> None:
    data = [{"description": "Оплата"}]

    result = process_bank_search(data, "кредит")

    assert result == []


def test_process_bank_operations_count() -> None:
    data = [
        {"description": "Перевод на карту"},
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
    ]

    categories = ["Перевод", "Оплата"]

    result = process_bank_operations(data, categories)

    assert result["Перевод"] == 2
    assert result["Оплата"] == 1


def test_process_bank_operations_empty() -> None:
    data: list[dict[str, Any]] = []

    result = process_bank_operations(data, ["Перевод"])

    assert result["Перевод"] == 0
