import pytest
import allure
from playwright.sync_api import sync_playwright
from utils.string_utils import format_test_name
from loguru import logger

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser_page(request, playwright_instance):
    browser_name = request.config.getoption("--browser") or "chromium"
    browser = getattr(playwright_instance, browser_name).launch(headless=False)
    page = browser.new_page()

    formatted_name = format_test_name(request.node.name, browser_name)

    # Allure: Set dynamic title
    allure.dynamic.title(formatted_name)

    # NEW → Group by browser in Allure
    allure.label("browser", browser_name)

    # NEW → Group by category (marker name)
    for mark in request.node.iter_markers():
        allure.label("category", mark.name)

    # Logging
    logger.info(f"Starting test: {formatted_name}")

    yield page, formatted_name

    # Screenshot on teardown
    screenshot_path = f"reports/{formatted_name}.png"
    page.screenshot(path=screenshot_path)
    allure.attach.file(
        screenshot_path,
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    logger.info(f"Screenshot saved to {screenshot_path}")

    browser.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chromium",
        help="Browser to run tests on: chromium, firefox, webkit"
    )
