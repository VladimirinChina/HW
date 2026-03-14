from __future__ import annotations

from typing import Any

import pytest

from src.external_api import convert_to_rub


def test_convert_rub_without_api() -> None:
    """Если валюта RUB — API не вызывается."""

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "RUB"},
        }
    }

    result = convert_to_rub(transaction)

    assert result == 100.0


def test_convert_usd_to_rub(monkeypatch: pytest.MonkeyPatch) -> None:
    """Конвертация USD → RUB через API."""

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"},
        }
    }

    class MockResponse:
        status_code = 200

        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, Any]:
            return {
                "success": True,
                "result": 900.0,
            }

    def mock_get(*args: Any, **kwargs: Any) -> MockResponse:
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    result = convert_to_rub(transaction)

    assert result == 900.0


def test_convert_eur_to_rub(monkeypatch: pytest.MonkeyPatch) -> None:
    """Конвертация EUR → RUB через API."""

    transaction = {
        "operationAmount": {
            "amount": "5",
            "currency": {"code": "EUR"},
        }
    }

    class MockResponse:
        status_code = 200

        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, Any]:
            return {
                "success": True,
                "result": 500.0,
            }

    def mock_get(*args: Any, **kwargs: Any) -> MockResponse:
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    result = convert_to_rub(transaction)

    assert result == 500.0


def test_api_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    """Если API возвращает success=False."""

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"},
        }
    }

    class MockResponse:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, Any]:
            return {"success": False}

    def mock_get(*args: Any, **kwargs: Any) -> MockResponse:
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    with pytest.raises(RuntimeError):
        convert_to_rub(transaction)


def test_unsupported_currency() -> None:
    """Неподдерживаемая валюта вызывает ValueError."""

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "GBP"},
        }
    }

    with pytest.raises(ValueError):
        convert_to_rub(transaction)
