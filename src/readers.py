from __future__ import annotations

from typing import Any, cast

import pandas as pd


def read_csv(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает финансовые операции из CSV файла.

    :param file_path: путь к CSV файлу
    :return: список словарей с транзакциями
    """

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            return []

        result = df.to_dict(orient="records")
        return cast(list[dict[str, Any]], result)

    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


def read_excel(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает финансовые операции из Excel файла.

    :param file_path: путь к Excel файлу
    :return: список словарей с транзакциями
    """

    try:
        df = pd.read_excel(file_path)

        if df.empty:
            return []

        result = df.to_dict(orient="records")
        return cast(list[dict[str, Any]], result)

    except (FileNotFoundError, ValueError):
        return []
