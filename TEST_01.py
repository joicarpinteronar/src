# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestUntitled():
    def setup_method(self, method):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path=r"D:\driver\chromedriver.exe")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("http://poseidon01/primeread")
        self.driver.set_window_size(1378, 737)
        self.driver.find_element(By.CSS_SELECTOR, "#UserName .dxic").click()
        self.driver.find_element(By.ID, "UserName_I").click()
        self.driver.find_element(By.ID, "UserName_I").send_keys("zulay.bonilla")
        self.driver.find_element(By.ID, "LoginForm").click()
        self.driver.find_element(By.ID, "Password_I").send_keys("zulay.bonilla")
        self.driver.find_element(By.ID, "LoginForm").c
        self.driver.find_element(By.CSS_SELECTOR, ".ps-basic-button-blue").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ps-basic-button-blue")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ps-basic-button-blue").click()
        self.driver.close()

