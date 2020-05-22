from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Web.selenium_wework_main.Contacts import Contacts
from Web.selenium_wework_main.addmember import Addmember


class MainPage:

    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    def goto_contacts(self):
        sleep(2)
        self._driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        sleep(3)
        self._driver.find_element(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return Addmember(self._driver)