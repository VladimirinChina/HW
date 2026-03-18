from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.logger_config import setup_logger

logger = setup_logger("utils")


def load_operations(file_path: str) -> list[dict[str, Any]]:
    """
    Загружает финансовые операции из JSON файла.

    Если файл пустой, не найден или содержит не список,
    возвращает пустой список.
    """

    logger.info("Loading operations from %s", file_path)

    try:
        path = Path(file_path)

        if not path.exists():
            logger.warning("File not found: %s", file_path)
            return []

        if path.stat().st_size == 0:
            logger.warning("File is empty: %s", file_path)
            return []

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning("JSON is not a list in file: %s", file_path)
            return []

        logger.info("Successfully loaded %d operations", len(data))
        return data

    except json.JSONDecodeError:
        logger.error("Invalid JSON format in file: %s", file_path)
        return []

    except OSError:
        logger.error("OS error while reading file: %s", file_path)
        return []
