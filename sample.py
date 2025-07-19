"""Sample module with intentional bugs for Nova Solve demo."""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers (with a bug)."""
    return a + b  # Bug: should be a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        return None  # Bug: should raise ZeroDivisionError
    return a / b

def concatenate(str1, str2):
    """Concatenate two strings (with a bug)."""
    return str1 + " " + str2.upper()  # Bug: shouldn't uppercase str2
