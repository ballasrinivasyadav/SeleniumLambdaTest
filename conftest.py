import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

@pytest.fixture
def setup(request):
    driver = webdriver.Chrome("C:\\Users\\Srinivas\\PycharmProjects\\SeleniumPython101\\Driver\\chromedriver.exe")
    driver.get("https://www.lambdatest.com/selenium-playground/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


