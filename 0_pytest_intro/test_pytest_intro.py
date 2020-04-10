# Создание тестовых файлов
import pytest
import random


def test_one(function_fixture, class_fixture, module_fixture, session_fixture):
    """Первый тест первого файла, тут мы выводим пересечения множеств"""
    k = {1, 2, 3, 4}
    c = {3, 4, 5, 6}
    print(k.intersection(c))
    print(c.intersection(k))


def test_two(function_fixture, class_fixture, module_fixture, session_fixture):
    """Второй тест первого файла, тут мы сравниваем два числа"""
    print("Будем исполнять фикстуру класса, смотрим на очередность")
    assert 4 == 5


pass