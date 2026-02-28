import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(
        operations: list[dict[str, str | int]]
) -> None:
    result = filter_by_state(operations, "EXECUTED")

    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("PENDING", 1),
        ("CANCELED", 0),
    ],
)
def test_filter_by_state_parametrized(
        operations: list[dict[str, str | int]],
        state: str,
        expected_count: int,
) -> None:
    result = filter_by_state(operations, state)
    assert len(result) == expected_count


def test_filter_by_state_empty_list() -> None:
    result = filter_by_state([], "EXECUTED")
    assert result == []


def test_sort_by_date_descending(
        operations: list[dict[str, str | int]]
) -> None:
    result = sort_by_date(operations)

    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(
        operations: list[dict[str, str | int]]
) -> None:
    result = sort_by_date(operations, reverse=False)

    dates = [op["date"] for op in result]
    assert dates == sorted(dates)
