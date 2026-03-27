from __future__ import annotations

import re
from typing import Any


def process_bank_search(
    data: list[dict[str, Any]],
    search: str,
) -> list[dict[str, Any]]:
    """
    Фильтрует список операций по строке в описании (через regex).

    :param data: список транзакций
    :param search: строка поиска
    :return: отфильтрованный список
    """

    pattern = re.compile(search, re.IGNORECASE)

    return [
        item
        for item in data
        if pattern.search(item.get("description", ""))
    ]


def process_bank_operations(
    data: list[dict[str, Any]],
    categories: list[str],
) -> dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    :param data: список транзакций
    :param categories: список категорий
    :return: словарь {категория: количество}
    """

    result = {category: 0 for category in categories}

    for item in data:
        description = item.get("description", "")

        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1

    return result
