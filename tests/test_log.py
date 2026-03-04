from pathlib import Path

import pytest

from src.decorators import log


def test_log_decorator_console_success(capsys: pytest.CaptureFixture[str],) -> None:
    """Тест успешного выполнения с логированием в консоль."""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(5, 3)
    captured = capsys.readouterr()

    assert result == 8
    assert "add ok" in captured.out
    assert captured.err == ""


def test_log_decorator_console_error(capsys: pytest.CaptureFixture[str],) -> None:
    """Тест ошибки с логированием в консоль."""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_decorator_file_success(tmp_path: Path) -> None:
    """Тест успешного выполнения с логированием в файл."""

    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 2)

    assert result == 4
    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")
    assert "add ok" in content


def test_log_decorator_file_error(tmp_path: Path) -> None:
    """Тест ошибки с логированием в файл."""

    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "divide error" in content
    assert "Inputs: (1, 0), {}" in content


def test_log_multiple_calls_file(tmp_path: Path) -> None:
    """Тест нескольких последовательных вызовов."""

    log_file = tmp_path / "multi_log.txt"

    @log(filename=str(log_file))
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 1)
    add(2, 2)
    add(3, 3)

    content = log_file.read_text(encoding="utf-8").splitlines()

    assert len(content) == 3
    assert all("add ok" in line for line in content)


def test_no_console_output_when_filename_set(
        capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None:
    """При переданном filename в консоль ничего не выводится."""

    log_file = tmp_path / "silent_log.txt"

    @log(filename=str(log_file))
    def add(a: int, b: int) -> int:
        return a + b

    add(10, 5)
    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""
