from leap import is_leap

def test_is_leap():
    assert is_leap(2000) == True
    assert is_leap(2023) == False
    assert is_leap(2024) == True
    assert is_leap(1900) == False