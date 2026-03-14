from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from src.utils import load_operations


def test_load_operations_success(tmp_path: Path) -> None:
    """Тест успешной загрузки списка операций."""

    file = tmp_path / "operations.json"
    file.write_text('[{"id": 1}, {"id": 2}]', encoding="utf-8")

    result: list[dict[str, Any]] = load_operations(str(file))

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1


def test_load_operations_file_not_found() -> None:
    """Если файл не найден — возвращается пустой список."""

    result = load_operations("non_existing_file.json")

    assert result == []


def test_load_operations_empty_file(tmp_path: Path) -> None:
    """Если файл пустой — возвращается пустой список."""

    file = tmp_path / "operations.json"
    file.write_text("", encoding="utf-8")

    result = load_operations(str(file))

    assert result == []


def test_load_operations_not_list(tmp_path: Path) -> None:
    """Если JSON содержит не список — возвращается пустой список."""

    file = tmp_path / "operations.json"
    file.write_text('{"id": 1}', encoding="utf-8")

    result = load_operations(str(file))

    assert result == []


def test_load_operations_invalid_json(tmp_path: Path) -> None:
    """Если JSON поврежден — возвращается пустой список."""

    file = tmp_path / "operations.json"
    file.write_text("{invalid json}", encoding="utf-8")

    result = load_operations(str(file))

    assert result == []


def test_load_large_file(tmp_path: Path) -> None:
    """Тест загрузки большого файла с множеством операций."""

    large_data = [{"id": i, "amount": i * 100} for i in range(1000)]

    file_path = tmp_path / "large.json"
    file_path.write_text(json.dumps(large_data), encoding="utf-8")

    result = load_operations(str(file_path))

    assert len(result) == 1000
    assert result == large_data


def test_load_file_with_os_error(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Тест обработки OSError при чтении файла."""

    file_path = tmp_path / "operations.json"
    file_path.write_text("[]", encoding="utf-8")

    def mock_open(*args: Any, **kwargs: Any) -> Any:
        raise OSError("Permission denied")

    monkeypatch.setattr("pathlib.Path.open", mock_open)

    result = load_operations(str(file_path))

    assert result == []


def test_load_file_with_json_decode_error(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Тест обработки JSONDecodeError."""

    file_path = tmp_path / "operations.json"
    file_path.write_text("{}", encoding="utf-8")

    def mock_json_load(*args: Any, **kwargs: Any) -> Any:
        raise json.JSONDecodeError("Invalid JSON", "", 0)

    monkeypatch.setattr(json, "load", mock_json_load)

    result = load_operations(str(file_path))

    assert result == []


@pytest.mark.parametrize(
    "file_content",
    [
        "",
        "   ",
        "\n",
        "\t",
    ],
)
def test_load_whitespace_files(tmp_path: Path, file_content: str) -> None:
    """Тест загрузки файлов, содержащих только пробельные символы."""

    file_path = tmp_path / "whitespace.json"
    file_path.write_text(file_content, encoding="utf-8")

    result = load_operations(str(file_path))

    assert result == []
    assert file_path.exists()
