from selenium.webdriver.support.events import AbstractEventListener
from basic.selenium_basic import SeleniumBasic


class MyListener(AbstractEventListener):

    def before_click(self, element, driver):
        SeleniumBasic(driver).delete_specified_cookie('ak_bmsc')

    def after_click(self, element, driver):
        SeleniumBasic(driver).delete_specified_cookie('ak_bmsc')