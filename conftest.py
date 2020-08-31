import pytest
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def setup_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
