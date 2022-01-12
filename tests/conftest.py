import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_name=="firefox":
        print("firefoxbrowser")
    elif browser_name=="IE":
        print("IE BROWSER")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver=driver
    yield
    driver.close()