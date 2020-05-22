import pytest
from selenium import webdriver
from time import *

from selenium.webdriver import TouchActions

from Web.common import Base


class Testtouch(Base):
    # def setup(self):
    #     """如果环境变量中没有driver地址可以通过以下方式添加"""
    #     #self.driver = webdriver.Chrome(executable_path="driver的路径")
    #     option = webdriver.ChromeOptions()
    #     option.add_experimental_option('w3c', False)
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.maximize_window()
    #     """隐式等待，最多等待5秒，5秒内如果找到元素则会继续执行不再继续等待"""
    #     """全局的，下面每回执行的时候都会等待"""
    #     self.driver.implicitly_wait(5)
    #
    #
    # def teardown(self):
    #     self.driver.quit()

    def test_touchaction(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_id('kw')
        ele.send_keys("selenium测试")
        self.driver.find_element_by_id('su').click()
        action = TouchActions(self.driver)
        action.scroll_from_element(ele, 0, 10000).perform()

    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.find_element_by_id('user_login').send_keys('123')
        self.driver.find_element_by_id('user_password').send_keys('123')
        self.driver.find_element_by_name('commit').click()

    def test_windows(self):
        self.driver.get('http://www.baidu.com')
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('ce')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('1232')
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('121212')
        self.driver.switch_to.window(windows[0])
        sleep(3)
    def test_frame(self):
        # self.driver.get('https://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols')
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)
        #self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(1)




if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_touchactions.py::Testtouch::test_frame'])
