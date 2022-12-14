import pytest
from selenium import webdriver

from config.config import TestData
from selenium.webdriver.chrome.service import Service

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):

    if request.param == "chrome":
        #web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        s = Service(TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=s)
        web_driver.maximize_window()

    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
        web_driver.set_window_size(1400, 900)
    request.cls.driver = web_driver
    yield
    web_driver.quit()