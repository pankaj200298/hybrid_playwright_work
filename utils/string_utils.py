def format_test_name(test_name: str, browser: str = "chrome") -> str:
    """Format a test name for reporting."""
    return f"[{browser.upper()}]_{test_name.strip().replace(' ', '_')}"
