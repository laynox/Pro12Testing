from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Web.selenium_wework_main.addmember import Addmember


class Contacts:
    def __init__(self, driver: WebDriver):
        self._driver = driver


    def find_addmember(self):

        sleep(5)
        self._driver.find_element(By.XPATH, '//*[@id="js_contacts96"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        return Addmember(self._driver)