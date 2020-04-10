import pytest


def f(ass):
    assert ass + "big" == "assbig"


def test_one_f(function_fixture, class_fixture, module_fixture, session_fixture):
    """В данной функции мы сравниваем большие жопы"""
    print(f"\n Выполнение внутренней части второго файла")
    f("ass")