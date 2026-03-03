import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "Visa Platinum 1234567812345678",
            "Visa Platinum 1234 56** **** 5678",
        ),
        (
            "MasterCard 1111222233334444",
            "MasterCard 1111 22** **** 4444",
        ),
    ],
)
def test_mask_account_card_card(
    input_data: str,
    expected: str,
) -> None:
    assert mask_account_card(input_data) == expected


def test_mask_account_card_account() -> None:
    input_data = "Счет 12345678"
    expected = "Счет **5678"
    assert mask_account_card(input_data) == expected


def test_mask_account_card_account_lowercase() -> None:
    input_data = "счет 12345678"
    expected = "счет **5678"
    assert mask_account_card(input_data) == expected


def test_get_date_standard() -> None:
    input_date = "2025-04-12T02:14:19.478365"
    expected = "12.04.2025"
    assert get_date(input_date) == expected


def test_get_date_without_time() -> None:
    input_date = "2025-04-12"
    expected = "12.04.2025"
    assert get_date(input_date) == expected
