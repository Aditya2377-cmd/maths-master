from project import is_valid_op, is_valid_level, is_valid_score


def test_is_valid_op():
    assert is_valid_op("A") == True
    assert is_valid_op("Z") == False


def test_is_valid_level():
    assert is_valid_level(1) == True
    assert is_valid_level(9) == False


def test_is_valid_score():
    result = is_valid_score(5)
    assert isinstance(result, int) == True 
    assert result >= 0  