from __future__ import annotations

from src.logger_config import setup_logger

logger = setup_logger("masks")


def get_mask_card_number(number: int) -> str:
    """
    Преобразование числа в маску.
    :param number: данный параметр принимает целочисленный тип данных
    :return: строку в формате XXXX XX** **** XXXX
    """

    if not isinstance(number, int):
        logger.error("Invalid card number type: %s", type(number))
        raise TypeError("Card number must be integer")

    logger.info("Masking card number")

    conv_str = str(number)

    if len(conv_str) < 10:
        logger.error("Card number is too short: %s", conv_str)
        raise ValueError("Card number is too short")

    count_stars = "*" * (len(conv_str) - 10)
    split_number = f"{conv_str[:6]}{count_stars}{conv_str[-4:]}"

    parts = [split_number[i:i + 4] for i in range(0, len(split_number), 4)]
    result = " ".join(parts)

    logger.info("Masking card number: %s", result)
    return result


def get_mask_account(number: int) -> str:
    """
    Преобразование числа в маску счета.
    :param number: данный параметр принимает целочисленный тип данных
    :return: строку в формате **XXXX
    """

    if not isinstance(number, int):
        logger.error("Invalid account number type: %s", type(number))
        raise TypeError("Account number must be integer")

    logger.info("Masking account number")

    conv_str = str(number)

    if len(conv_str) < 4:
        logger.warning("Account number is too short: %s", conv_str)

    result = f"**{conv_str[-4:]}"

    logger.info("Masked account: %s", result)
    return result
