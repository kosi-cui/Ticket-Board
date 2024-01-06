import pytest

def add_numbers(a, b):
    return a + b

def test_add_positive_numbers():
    assert add_numbers(1, 2) == 3

def test_add_negative_numbers():
    assert add_numbers(-1, -2) == -3

def test_add_zero():
    assert add_numbers(0, 0) == 0