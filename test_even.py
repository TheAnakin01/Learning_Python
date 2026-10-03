from even import is_even

def test_iseven():
    assert is_even(4) == True
    assert is_even(3) == False
    assert is_even(-3) == False
    assert is_even(0) == True