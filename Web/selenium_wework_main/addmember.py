from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class Addmember:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        sleep(1)
        self._driver.find_element_by_id('username').send_keys('test1')
        self._driver.find_element_by_id("memberAdd_acctid").send_keys('test1')
        self._driver.find_element_by_xpath("//*[@id='js_contacts63']/div/div[2]/div/div[4]/div/form/div[1]/a[2]")
        sleep(3)
        return True

    # def get_member(self):

