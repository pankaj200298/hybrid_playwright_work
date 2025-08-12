from utils.error_handler import safe_divide

def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(5, 0) == "Cannot divide by zero"
