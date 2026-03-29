from __future__ import annotations

from typing import Any

from src.filters import process_bank_search
from src.masks import get_mask_account, get_mask_card_number
from src.utils import load_operations

VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def format_transaction(op: dict[str, Any]) -> str:
    """Форматирует транзакцию для вывода."""

    description = op.get("description", "")
    date = op.get("date", "")[:10]

    from_acc = op.get("from")
    to_acc = op.get("to")

    result_lines = [f"{date} {description}"]

    if isinstance(from_acc, str) and isinstance(to_acc, str):
        if "Счет" in from_acc:
            masked_from = get_mask_account(int(from_acc.split()[-1]))
        else:
            masked_from = get_mask_card_number(int(from_acc.split()[-1]))

        if "Счет" in to_acc:
            masked_to = get_mask_account(int(to_acc.split()[-1]))
        else:
            masked_to = get_mask_card_number(int(to_acc.split()[-1]))

        result_lines.append(f"{masked_from} -> {masked_to}")

    elif isinstance(to_acc, str):
        if "Счет" in to_acc:
            masked_to = get_mask_account(int(to_acc.split()[-1]))
            result_lines.append(masked_to)

    amount = op.get("operationAmount", {})
    value = amount.get("amount", "")
    currency = amount.get("currency", {}).get("code", "")

    result_lines.append(f"Сумма: {value} {currency}")

    return "\n".join(result_lines)


def main() -> None:
    print(
        "Привет! Добро пожаловать в программу работы\n"
        "с банковскими транзакциями.\n"
        "Выберите источник:\n"
        "1. JSON\n2. CSV\n3. XLSX"
    )

    choice = input()

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_operations("data/operations.json")
    else:
        print("Пока поддерживается только JSON")
        return

    # --- статус ---
    while True:
        status = input(
            "Введите статус (EXECUTED, CANCELED, PENDING):\n"
        ).upper()

        if status not in VALID_STATUSES:
            print(f'Статус "{status}" недоступен.')
            continue

        break

    filtered = [
        op for op in data
        if op.get("state", "").upper() == status
    ]

    print(f'Операции отфильтрованы по статусу "{status}"')

    # --- сортировка ---
    if input("Сортировать по дате? да/нет\n").lower() == "да":
        reverse = input("По убыванию? да/нет\n").lower() == "да"

        filtered.sort(
            key=lambda x: x.get("date", ""),
            reverse=reverse,
        )

    # --- только рубли ---
    if input("Только RUB? да/нет\n").lower() == "да":
        filtered = [
            op for op in filtered
            if op.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    # --- поиск ---
    if input("Фильтр по слову? да/нет\n").lower() == "да":
        word = input("Введите слово:\n")
        filtered = process_bank_search(filtered, word)

    # --- вывод ---
    print("\nРезультат:\n")

    if not filtered:
        print("Не найдено ни одной транзакции")
        return

    print(f"Всего операций: {len(filtered)}\n")

    for op in filtered:
        print(format_transaction(op))
        print()


if __name__ == "__main__":
    main()
