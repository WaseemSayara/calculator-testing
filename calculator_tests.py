import pytest

from calculator import *


@pytest.mark.parametrize("input1,input2,result", [(1, 2, 3), (9, -6, 3), (0, 66, 66)])
def test_addition_two_integers(input1, input2, result):
    assert Calculator.addition(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(1.6, 2, 3.6), (9.5, -6, 3.5), (5, 6.0, 11.0)])
def test_addition_integers_and_float(input1, input2, result):
    assert Calculator.addition(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(1.623, 2.2, 3.823), (9.5, -6.3, 3.2), (5.0, 6.0, 11.0)])
def test_addition_two_floats(input1, input2, result):
    assert Calculator.addition(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(1, 2, -1), (9, -6, 15), (0, 66, -66)])
def test_subtraction_two_integers(input1, input2, result):
    assert Calculator.subtraction(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(1.6, 2, -0.4), (9.5, -6, 15.5), (9, 6.0, 3.0)])
def test_subtraction_integers_and_float(input1, input2, result):
    assert Calculator.subtraction(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(3.623, 2.2, 1.423), (9.5, -6.3, 15.8), (5.0, 6.0, -1.0)])
def test_subtraction_two_floats(input1, input2, result):
    assert Calculator.subtraction(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(1, 2, 2), (9, -6, -54), (0, 66, 0)])
def test_multiply_two_integers(input1, input2, result):
    assert Calculator.multiply(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(1.6, 2, 3.2), (9.5, -6, -57.0), (9, 6.0, 54.0), (0, 1.6, 0)])
def test_multiply_integers_and_float(input1, input2, result):
    assert Calculator.multiply(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(3.623, 2.2, 7.9706), (9.5, -6.3, -59.85), (5.0, 6.0, 30.0)])
def test_multiply_two_floats(input1, input2, result):
    assert Calculator.multiply(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(4, 2, 2), (6, -2, -3), (0, 66, 0), (5, 2, 2.5), (8, 16, 0.5)])
def test_division_two_integers(input1, input2, result):
    assert Calculator.division(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(3.2, 2, 1.6), (9.6, -3, -3.2), (9, 6.0, 1.5), (0, 1.6, 0),
                                                  (1.5, 0, None)])
def test_division_integers_and_float(input1, input2, result):
    assert Calculator.division(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(12.16, 3.04, 4.0), (14.4, -3.2, -4.5), (5.0, 10.0, 0.5)])
def test_division_two_floats(input1, input2, result):
    assert Calculator.division(input1, input2) == result


@pytest.mark.parametrize("input1,input2,result", [(1, "5", None), (1, "A", None), ("1", "5", None)])
def test_string_input(input1, input2, result):
    assert Calculator.addition(input1, input2) == result
    assert Calculator.subtraction(input1, input2) == result
    assert Calculator.multiply(input1, input2) == result
    assert Calculator.division(input1, input2) == result
