import pytest

from app.income_calc import calculate_income

@pytest.mark.parametrize('summ,rate, period, expected', [
    (700000, 8, 12, 758100)

])
def test_income_calc(summ, rate, period, expected):
    actual = calculate_income(summ, rate, period)
    assert expected == actual
