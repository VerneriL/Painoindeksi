import questions


def test_static_get_user_integer(monkeypatch):
    user_input='100'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.get_input_integer('Luku: ', False) == (100, 'OK', 0, 'Conversion successful')

def test_static_get_user_integer_2(monkeypatch):
    user_input='100 v'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.get_input_integer('Luku: ', False) == (0, 'Error', 1, "invalid literal for int() with base 10: '100 v'")

def test_static_get_input_boolean(monkeypatch):
    user_input='y'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.get_input_boolean('Y/N','Y', 'N', False) == (True, 'OK', 0, 'Conversion successful')

def test_static_get_input_boolean_error(monkeypatch):
    user_input='1'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.get_input_boolean('Y/N', 'Y', 'N', False) == ('N/A,', 'Error', 1, 'Unable to convert to boolean')

def test_static_get_input_float(monkeypatch):
    user_input = '1.5'
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.get_input_float('Luku: ', False) == (1.5, 'OK', 0, 'Conversion successful')

def test_static_get_input_float_replace(monkeypatch):
    user_input = "74,6"
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.get_input_float('Luku: ', False) == (74.6, 'OK', 0, 'Conversion successful')

def test_static_get_input_float_error_2(monkeypatch):
    user_input = "1.5v"
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.get_input_float('Luku: ', False) == (0, 'Error', 1, "could not convert string to float: '1.5v'")

def test_ask_user_dictionary(monkeypatch):
    user_input = "Tyttö"
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.ask_user_dictionary('Sukupuoli: ', {"tyttö": 0}, False) == (0, 'OK', 0,  'Conversion successful')

def test_ask_user_dictionary_error(monkeypatch):
    user_input = "auto"
    monkeypatch.setattr('builtins.input', lambda _:user_input)
    assert questions.Question.ask_user_dictionary('Sukupuoli: ', {"tyttö": 0}, False) == ('N/A', 'Error', 1, "'auto'")