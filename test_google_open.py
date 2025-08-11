from playwright.sync_api import sync_playwright


def test_open_google():
    with sync_playwright() as p :
        browser =  p.chromium.launch(headless=False,slow_mo=100)
        # browser = context.new_context()
        page = browser.new_page()
        url =  "https://www.google.com"
        page.goto(url=url)
        page.fill("//textarea[@title='Search']","Playwright Python")
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)
        assert "Playwright" in page.title()
        browser.close()

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=100)
        page = browser.new_page()
        page.goto("https://google.com")
        page.fill("textarea[name='q']", "Playwright Python")
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)
        assert "Playwright" in page.title()
        browser.close()