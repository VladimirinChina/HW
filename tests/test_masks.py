import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (1111222233334444, "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number_standard(
        number: int,
        expected: str,
) -> None:
    assert get_mask_card_number(number) == expected


def test_get_mask_card_number_min_length() -> None:
    number = 1234567890
    result = get_mask_card_number(number)

    assert "1234567890" in result.replace(" ", "")


@pytest.mark.parametrize(
    "number, expected",
    [
        (12345678, "**5678"),
        (987654321, "**4321"),
    ],
)
def test_get_mask_account(
        number: int,
        expected: str,
) -> None:
    assert get_mask_account(number) == expected


def test_get_mask_account_short_number() -> None:
    number = 123
    assert get_mask_account(number) == "**123"
