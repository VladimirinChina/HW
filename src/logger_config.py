from __future__ import annotations

import logging
from pathlib import Path


def setup_logger(name: str) -> logging.Logger:
    """
    Создает и настраивает логгер для модуля.
    """

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / f"{name}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # чтобы не дублировались хендлеры
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
