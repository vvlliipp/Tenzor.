import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get("https://saby.ru/?redir=1")
    yield chrome
    chrome.quit()
