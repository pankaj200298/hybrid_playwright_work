from utils.string_utils import format_test_name

def test_format_test_name():
    result = format_test_name("Login Page Title Test", "firefox")
    assert result == "[FIREFOX]_Login_Page_Title_Test"
