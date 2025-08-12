import pytest

@pytest.mark.smoke
def test_demo_login(browser_page):
    page, _ = browser_page
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    assert "You logged into a secure area!" in page.text_content("#flash")

@pytest.mark.regression
def test_demo_invalid_login(browser_page):
    page, _ = browser_page
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "wrong_user")
    page.fill("#password", "wrong_pass")
    page.click("button[type='submit']")
    assert "Your username is invalid!" in page.text_content("#flash")
