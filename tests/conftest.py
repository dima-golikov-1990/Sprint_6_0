import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    browser.get('https://qa-scooter.praktikum-services.ru/')

    yield browser
    browser.quit()