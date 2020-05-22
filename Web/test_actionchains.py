import pytest
from selenium import webdriver
from time import *

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup(self):
        """如果环境变量中没有driver地址可以通过以下方式添加"""
        #self.driver = webdriver.Chrome(executable_path="driver的路径")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        """隐式等待，最多等待5秒，5秒内如果找到元素则会继续执行不再继续等待"""
        """全局的，下面每回执行的时候都会等待"""
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(.,'霍格沃兹测试学院')]").click()
        self.driver.find_element_by_css_selector(".topic-23346 .title > a").click()

    def test_wait(self):
        self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        """显示等待的两种方式"""
        # """自定义的函数一定要有一个参数"""
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1
        # WebDriverWait(self.driver, 10).until(wait)
        """使用webdriver自带的expected_conditions来进行条件判断"""
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))

        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        element_dblclick = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        ActionChains(self.driver).click(element_click).context_click(element_rightclick).double_click(element_dblclick).perform()
        sleep(3)

    def test_move_to(self):
        self.driver.get("https://www.baidu.com")
        element_moveto = self.driver.find_element(By.XPATH, '//*[@id="u1"]/span')
        ActionChains(self.driver).move_to_element(element_moveto).perform()
        sleep(3)

    """拖拽元素"""
    def test_dragelement(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_ele = self.driver.find_element(By.ID, 'dragger')
        drop_ele1 = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        drop_ele2 = self.driver.find_element(By.XPATH, '/html/body/div[3]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele1).perform()
        action.click_and_hold(drag_ele).release(drop_ele2).perform()
        sleep(3)

    def test_sendkey(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        action = ActionChains(self.driver)
        action.click(ele)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("Tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_actionchains.py::TestHogwarts::test_sendkey'])
