from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """
    Возвращает список операций, отфильтрованных по значению ключа 'state'.

    Если в словаре отсутствует ключ 'state', операция игнорируется.

    :param operations: Список словарей с данными операций
    :param state: Значение состояния операции для фильтрации
    :return: Новый список операций, соответствующих указанному состоянию
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(
    operations: list[dict[str, Any]],
    reverse: bool = True
) -> list[dict[str, Any]]:
    """
    Возвращает новый список операций, отсортированных по ключу 'date'.

    По умолчанию сортировка выполняется по убыванию
    (сначала самые новые операции).

    Если в словаре отсутствует ключ 'date',
    такая операция игнорируется.

    :param operations: Список словарей с данными операций
    :param reverse: Направление сортировки (True — по убыванию)
    :return: Новый отсортированный список операций
    """
    return sorted(
        (operation for operation in operations if operation.get("date")),
        key=lambda operation: operation["date"],
        reverse=reverse,
    )
