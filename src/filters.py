from __future__ import annotations

import re
from collections import Counter
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
        if pattern.search(str(item.get("description", "")))
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

    descriptions = [
        str(item.get("description", "")).lower()
        for item in data
    ]

    counter: Counter[str] = Counter()

    for description in descriptions:
        for category in categories:
            if category.lower() in description:
                counter[category] += 1

    return dict(counter)
