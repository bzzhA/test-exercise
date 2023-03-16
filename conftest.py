from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def driver_factory(request):
    if request.param == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()
    elif request.param == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

