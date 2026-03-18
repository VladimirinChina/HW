from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.logger_config import setup_logger

logger = setup_logger("utils")


def load_operations(file_path: str) -> list[dict[str, Any]]:
    """
    Загружает финансовые операции из JSON файла.
    """

    try:
        path = Path(file_path)

        if not path.exists():
            logger.warning("File not found")
            return []

        if path.stat().st_size == 0:
            logger.warning("File is empty")
            return []

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning("JSON is not a list")
            return []

        logger.info(f"Loaded {len(data)} operations")
        return data

    except json.JSONDecodeError:
        logger.error("Invalid JSON format")
        return []

    except OSError as e:
        logger.error(f"OS error: {e}")
        return []
