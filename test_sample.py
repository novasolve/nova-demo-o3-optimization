from sample import add, multiply

def test_add():
    """Test the addition function."""
    assert add(2, 2) == 4
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_multiply():
    """Test the multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
