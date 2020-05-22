import shelve

from selenium import webdriver
from time import *


class TestWechart:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_chrome(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # db['cookie'] = self.driver.get_cookies()
        db = shelve.open("cookies")
        db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id('menu_contacts').click()
        db.close()
        sleep(5)