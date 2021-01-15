import pytest
from day01 import calc_fuel, calc_fuel_tot

@pytest.mark.parametrize("test_input, expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_calc_fuel(test_input, expected):
    assert calc_fuel(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(14, 2), (1969, 966), (100756, 50346)])
def test_calc_fuel_tot(test_input, expected):
    assert calc_fuel_tot(test_input) == expected