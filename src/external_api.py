from __future__ import annotations

import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях.

    Если валюта RUB — возвращается исходная сумма.
    Если валюта USD или EUR — выполняется запрос к API для конвертации.
    """

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency not in {"USD", "EUR"}:
        raise ValueError(f"Unsupported currency: {currency}")

    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount,
    }

    headers = {
        "apikey": API_KEY,
    }

    response = requests.get(API_URL, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("success"):
        raise RuntimeError("Currency conversion failed")

    result = data.get("result")

    if result is None:
        raise RuntimeError("Invalid API response")

    return float(result)
