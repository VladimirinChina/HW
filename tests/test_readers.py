from __future__ import annotations

from unittest.mock import patch

import pandas as pd

from src.readers import read_csv, read_excel


def test_read_csv_success() -> None:
    data = [{"id": 1}, {"id": 2}]
    df = pd.DataFrame(data)

    with patch("pandas.read_csv", return_value=df):
        result = read_csv("fake.csv")

    assert result == data


def test_read_csv_empty() -> None:
    df = pd.DataFrame()

    with patch("pandas.read_csv", return_value=df):
        result = read_csv("fake.csv")

    assert result == []


def test_read_csv_file_not_found() -> None:
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = read_csv("fake.csv")

    assert result == []


def test_read_excel_success() -> None:
    data = [{"id": 1}, {"id": 2}]
    df = pd.DataFrame(data)

    with patch("pandas.read_excel", return_value=df):
        result = read_excel("fake.xlsx")

    assert result == data


def test_read_excel_empty() -> None:
    df = pd.DataFrame()

    with patch("pandas.read_excel", return_value=df):
        result = read_excel("fake.xlsx")

    assert result == []


def test_read_excel_file_not_found() -> None:
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = read_excel("fake.xlsx")

    assert result == []
