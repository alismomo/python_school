"""
Test for lab11_adzhoha.py file. Alisa Dzhoha. This test file checks fi the code from the file works correctly and catches the exceptions. 11/08/2025

"""
from lab11_adzhoha import calculating_degree_rotation

def test_positive_number_input():
  assert calculating_degree_rotation(100) == 100
  assert calculating_degree_rotation(460) == 100
  assert calculating_degree_rotation(820) == 100

def test_negative_number_input():
  assert calculating_degree_rotation(-100) == 260
  assert calculating_degree_rotation(-460) == 260
  assert calculating_degree_rotation(-820) == 260

def test_edge_number_input():
  assert calculating_degree_rotation(0) == 0
  assert calculating_degree_rotation(360) == 0
  assert calculating_degree_rotation(361) == 1
  assert calculating_degree_rotation(721) == 1

def test_input_as_string():
  assert calculating_degree_rotation('cat') == 'Your input is invalid, please provide a number'

def test_string_digits_as_an_input():
  assert calculating_degree_rotation('100') == 100
  assert calculating_degree_rotation('460') == 100

def test_empty_input():
  assert calculating_degree_rotation('') == 'Your input is invalid, please provide a number'

def test_input_as_symbols():
  assert calculating_degree_rotation({}) == 'Your input is invalid, please provide a number'

def test_white_spaces_in_input():
  assert calculating_degree_rotation(' 100 ') == 100

def test_large_number_as_an_input():
  assert calculating_degree_rotation(999999999999) == 279
 
def test_negative_one():
    assert calculating_degree_rotation(-1) == 359

def test_negative_edge_cases():
    assert calculating_degree_rotation(-361) == 359

def test_input_as_calculation():
  assert calculating_degree_rotation(50 + 50) == 100