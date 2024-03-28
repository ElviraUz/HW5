import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1352
    browser.config.window_width = 878
    yield
    browser.quit()
