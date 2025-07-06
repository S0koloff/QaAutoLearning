import logging
import allure

from calculator import Calculator
import pytest

@pytest.fixture
def calc():
    return Calculator()

@allure.feature("Calculator")
@allure.story("Addition")
def test_addition(calc):
    logging.info("Provetka slogeniya")
    result = calc.add(2, 3)
    logging.info(f"Result: {result}")
    assert result == 5

@allure.feature("Calculator")
@allure.story("Division")
def test_division(calc):
    assert calc.divide(10, 2) == 5

@allure.feature("Calculator")
@allure.story("Divide by Zero")
def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (5, 7, 12),
    (-3, 3, 0),
    (100, 200, 300)
])
@allure.feature("Calculator")
@allure.story("Add One")
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

@allure.feature("Calculator")
@allure.story("Add")
def testadd(calc):
    logging.info("Provetka slogeniya")
    result = calc.add(5, 7)
    logging.info(f"Result: {result}")
    assert result == 12