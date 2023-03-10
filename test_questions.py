import questions
import pytest

def test_get_input_integer(monkeypatch):
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    question = questions.Question('Luku: ')
    assert question.get_input_integer(False) == (100, 'OK', 0, 'Conversion successful')

def test_get_input_integer_2(monkeypatch):
    user_input='100 v'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    question = questions.Question('Luku: ')
    assert question.get_input_integer(False) == (0, 'Error', 1, "invalid literal for int() with base 10: '100 v'")

def test_get_input_boolean(monkeypatch):
    user_input='y'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    question = questions.Question('Y/N')
    assert question.get_input_boolean('Y', 'N', False) == (True, 'OK', 0, 'Conversion successful')

def test_get_input_boolean_error(monkeypatch):
    user_input='1'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    question = questions.Question('Y/N')
    assert question.get_input_boolean('Y', 'N', False) == ('N/A,', 'Error', 1, 'Unable to convert to boolean')

def test_get_input_float(monkeypatch):
    user_input = '1.5'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    question = questions.Question('Luku: ')
    assert question.get_input_float(False) == (1.5, 'OK', 0, 'Conversion successful')

def test_get_input_float_error(monkeypatch):
    user_input = "74,6"
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    question = questions.Question('Luku: ')
    assert question.get_input_float(False) == (0, 'Error', 1, "could not convert string to float: '74,6'")

def test_get_input_float_error_2(monkeypatch):
    user_input = "1.5v"
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    question = questions.Question('Luku: ')
    assert question.get_input_float(False) == (0, 'Error', 1, "could not convert string to float: '1.5v'")


