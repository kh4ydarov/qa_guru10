import pytest
import os
from selene import browser, be, have


@pytest.fixture(scope='function', autouse=True)
def config_browser_window():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()





