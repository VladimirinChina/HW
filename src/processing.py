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
