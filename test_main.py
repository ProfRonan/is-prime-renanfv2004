import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input", ["0", "-1", "-2", "-10"],
)
def test_not_valid(monkeypatch: MonkeyPatch, test_input: list[str]):
    mocked_input = lambda prompt="": test_input

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Número inválido" in mocked_stdout.getvalue().strip()
    assert "Primo" not in mocked_stdout.getvalue().strip()
    assert "Não primo" not in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input", ["1", "4", "6", "8", "9", "10",
                   "12", "14", "15", "16", "18", "20"],
)
def test_not_prime(monkeypatch: MonkeyPatch, test_input: list[str]):
    mocked_input = lambda prompt="": test_input

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Número inválido" not in mocked_stdout.getvalue().strip()
    assert "Primo" not in mocked_stdout.getvalue().strip()
    assert "Não primo" in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input", ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29"],
)
def test_prime(monkeypatch: MonkeyPatch, test_input: list[str]):
    mocked_input = lambda prompt="": test_input

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Número inválido" not in mocked_stdout.getvalue().strip()
    assert "Primo" in mocked_stdout.getvalue().strip()
    assert "Não primo" not in mocked_stdout.getvalue().strip()
