import mathlib_4
import pytest

@pytest.mark.parametrize('test_input,test_output',
                        [
                            (5,25),
                            (9,81),
                            (10,100)
                        ]
                        )
def test_calc_square(test_input,test_output):
    square = mathlib_4.calc_square(test_input)
    assert square == test_output

# def test_calc_square2():
#     square = mathlib_4.calc_square(9)
#     assert square == 81

# def test_calc_square3():
#     square = mathlib_4.calc_square(10)
#     assert square == 100
