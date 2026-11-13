from bug3_logic import find_max


def test_find_max_last_element():
    assert find_max([70, 85, 60, 95]) == 95


def test_find_max_middle_element():
    assert find_max([70, 95, 60, 85]) == 95


def test_find_max_descending():
    assert find_max([95, 85, 70, 60]) == 95


def test_find_max_single_score():
    assert find_max([80]) == 80