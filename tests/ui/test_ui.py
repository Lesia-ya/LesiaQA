import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку https://github.com/login 
    driver.get("https://github.com/login")

        # Закриваємо браузер
    driver.close()
