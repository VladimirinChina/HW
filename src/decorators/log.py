from __future__ import annotations

from functools import wraps
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log(filename: str | None = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор для логирования выполнения функции.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            def write_log(message: str) -> None:
                if filename:
                    path = Path(filename)
                    path.parent.mkdir(parents=True, exist_ok=True)

                    with path.open("a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                write_log(f"{func.__name__} ok")
                return result
            except Exception as error:
                write_log(
                    f"{func.__name__} error: {error}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise

        return wrapper

    return decorator
