from basic.selenium_basic import SeleniumBasic
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from typing import List

from basic.util_s import Utilss


class   HomePageNavigation(SeleniumBasic):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__navig_links: str = '#mainNavigationFobs>li'
        self.NAVI_LINKS_TEXT = 'Women,Men,Beauty,Home,Furniture,Shoes,Handbags,Jewelry,Kids,Toys,Gifts,Own Your Style,Sale'


    def get_navig_links(self) -> List[WebElement]:
        return self.elements_visibility('css_1', self.__navig_links, 'Nav links in the header')

    def get_navigation_links_text(self) -> str:
        navi_links = self.get_navig_links()
        navi_links_text = self.get_text_from_webelements1(navi_links)
        return Utilss.join_string(navi_links_text)

    def get_nav_links_by_title(self, title) -> WebElement:
        elements1 = self.get_navig_links()
        return self.get_elem_by_text(elements1, title)