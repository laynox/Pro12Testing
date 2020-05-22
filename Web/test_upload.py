from selenium.webdriver import ActionChains

from Web.common import Base
from time import *

class Testuplosd(Base):

    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        """必须上传元素是input标签下，才可以使用send_keys"""
        self.driver.find_element_by_id('stfile').send_keys('/Users/nox/Downloads/pic/67ab7c99065f367df423bdcb08b6c28b.jpg')
        sleep(10)

    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        ele1 = self.driver.find_element_by_id('draggable')
        ele2 = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1, ele2).perform()
        self.driver.switch_to_alert().accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(1)

