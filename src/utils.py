from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_operations(file_path: str) -> list[dict[str, Any]]:
    """
    Загружает финансовые операции из JSON файла.

    Если файл пустой, не найден или содержит не список,
    возвращает пустой список.
    """

    try:
        path = Path(file_path)

        if not path.exists():
            return []

        if path.stat().st_size == 0:
            return []

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []

        return data

    except (json.JSONDecodeError, OSError):
        return []
