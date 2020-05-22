from Web.common import Base
from time import *
import pytest

class TestJS(Base):

    def test_scroll(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        ele = self.driver.execute_script('return document.getElementById("su")')
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath('//*[@id="page"]/a[10]').click()
        sleep(3)
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_data_time(self):
        self.driver.get('http://www.12306.cn')
        self.driver.execute_script("ele=document.getElementById('train_date');ele.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

if __name__ == '__main__':
    pytest.main()
