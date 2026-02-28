from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Принимает строку с типом и номером карты или счета (например, "Visa Platinum 9843940329342112"
    или "Счет 65847364859384756381") и возвращает строку с замаскированным номером.
    :param data: строка с названием и номером карты или счета
    :return: строка с замаскированным номером.
    """

    # Отделяем номер (он всегда в конце строки)
    parts = data.split()
    number = int(parts[-1])  # преобразовал в int, потому что masks.py ожидает int
    name = " ".join(parts[:-1])

    # Если это счет
    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате ISO
    (YYYY-MM-DDTHH:MM:SS) в формат ДД.ММ.ГГГГ.

    :param date_string: строка с датой, например "2025-04-12T02:14:19.478365"
    :return: строка с датой в формате "12.04.2025"
    """
    # Нужно взять только часть до символа T
    date_part = date_string.split("T")[0]

    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
