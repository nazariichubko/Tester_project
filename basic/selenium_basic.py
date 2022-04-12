from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class SeleniumBasic:
    def __init__(self, driver):
        self.driver = driver
        self.__thewait = WebDriverWait(driver, 12, 0.3, ignored_exceptions=StaleElementReferenceException)

    def __choose_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locate = {'css_1': By.CSS_SELECTOR,
                  'xpath_1': By.XPATH,
                  'class_1': By.CLASS_NAME,
                  'id_1': By.ID,
                  'link_text_1': By.LINK_TEXT,
                  'name_1': By.NAME,
                  'par_link_text_1': By.PARTIAL_LINK_TEXT,
                  'tag_name_1': By.TAG_NAME
        }
        return locate[find_by]

    def elem_visibility(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__thewait.until(ec.visibility_of_element_located((self.__choose_selenium_by(find_by), locator)), locator_name)

    def elem_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__thewait.until(ec.presence_of_element_located((self.__choose_selenium_by(find_by), locator)), locator_name)

    def elem_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__thewait.until_not(ec.invisibility_of_element_located((self.__choose_selenium_by(find_by), locator)), locator_name)

    def elements_visibility(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__thewait.until(ec.visibility_of_all_elements_located((self.__choose_selenium_by(find_by), locator)), locator_name)

    def elements_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__thewait.until(ec.presence_of_all_elements_located((self.__choose_selenium_by(find_by), locator)), locator_name)

    def get_text_from_webelements1(self, elements1: List[WebElement]) -> List[str]:
        return [element1.text for element1 in elements1]

    def get_elem_by_text(self, elements1 : List[WebElement], title: str) -> WebElement:
        title.lower()
        return [element1 for element1 in elements1 if element1.text == title][0]






