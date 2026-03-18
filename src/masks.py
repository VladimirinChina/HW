from src.logger_config import setup_logger

logger = setup_logger("masks")


def get_mask_card_number(number: int) -> str:
    logger.info("Masking card number")
    """
    Преобразование числа в маску.
    :param number: данный параметр принимает целочисленный тип данных
    :return: строку в формате XXXX XX** **** XXXX
    """
    conv_str = str(number)
    count_stars = "*" * (len(conv_str) - 10)
    split_number = f"{conv_str[:6]}{count_stars}{conv_str[-4:]}"

    res_l = []
    for i in range(0, len(split_number), 4):
        res_l.append(split_number[i:i + 4])

    result = " ".join(res_l)

    logger.info(f"Masking card number: {result}")
    return result


def get_mask_account(number: int) -> str:
    logger.info("Masking account number")

    """
    Преобразование числа в маску счета.
    :param number: данный параметр принимает целочисленный тип данных
    :return: строку в формате **XXXX
    """
    conv_str = str(number)
    result = f"**{conv_str[-4:]}"

    logger.info(f"Masked account: {result}")
    return result
