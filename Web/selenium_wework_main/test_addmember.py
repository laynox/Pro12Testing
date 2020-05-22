from Web.selenium_wework_main.main_page import MainPage


class Testaddmember:

    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        self.main.goto_contacts().add_member()