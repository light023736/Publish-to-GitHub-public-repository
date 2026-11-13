from bug3_logic import find_max


def test_find_max_when_max_is_last():
    assert find_max([70, 85, 60, 95]) == 95


def test_find_max_when_max_is_first():
    assert find_max([95, 85, 70, 60]) == 95


def test_find_max_when_max_is_middle():
    assert find_max([70, 95, 60, 85]) == 95


def test_find_max_single_element():
    assert find_max([80]) == 80


def test_find_max_negative_numbers():
    assert find_max([-10, -3, -7]) == -3