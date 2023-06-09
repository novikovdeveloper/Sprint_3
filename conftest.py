import random
import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def random_email():
    return "testtestov" + str(random.randint(1, 999)) + "@test.ru"


@pytest.fixture
def random_password():
    return str(random.randint(100000, 999999))