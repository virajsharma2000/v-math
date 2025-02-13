import pytest
from v_math import is_perfect_square

def test_is_perfect_square():
    # Perfect squares
    assert is_perfect_square(0) == True  # 0^2 = 0
    assert is_perfect_square(1) == True  # 1^2 = 1
    assert is_perfect_square(4) == True  # 2^2 = 4
    assert is_perfect_square(9) == True  # 3^2 = 9
    assert is_perfect_square(16) == True # 4^2 = 16
    assert is_perfect_square(25) == True # 5^2 = 25
    assert is_perfect_square(100) == True # 10^2 = 100
    assert is_perfect_square(1024) == True # 32^2 = 1024
    #assert is_perfect_square(999_999_000_000) == True # 999999^2

    # Non-perfect squares
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(10) == False
    assert is_perfect_square(99) == False
    assert is_perfect_square(200) == False
    assert is_perfect_square(999_999_000_001) == False

    # Negative numbers (should always return False)
    assert is_perfect_square(-1) == False
    assert is_perfect_square(-4) == False
    assert is_perfect_square(-16) == False

# Run tests using pytest
if __name__ == "__main__":
    pytest.main()
