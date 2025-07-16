"""Tests for sample module."""

import pytest
from sample import add, multiply, divide, concatenate


def test_add():
    """Test addition function."""
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_concatenate():
    """Test string concatenation."""
    assert concatenate("hello", "world") == "hello world"
    assert concatenate("Nova", "Solve") == "Nova Solve"
