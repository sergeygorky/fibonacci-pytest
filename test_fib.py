import pytest
from fib import fib


def test1_return_number():
    assert fib(0) == 0


def test2_return_number():
    assert fib(1) == 1


def test3_return_number():
    assert fib(9) == 34


def test4_return_number():
    assert fib(10) == 55
    