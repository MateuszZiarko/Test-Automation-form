import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_settings import TestSettings
from selenium.webdriver.chrome.service import Service


class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        path = "/usr/bin/chromedriver"
        service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)
        self.url = TestSettings.page_url
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()
