import time
from basic.selenium_basic import SeleniumBasic
import pytest

from pom.home_page_nav import HomePageNavigation


@pytest.mark.usefixtures('test_setup')
class TestLandingPage:

    def test_navi_links(self):
        homepage_navi = HomePageNavigation(self.driver)
        actual_link = homepage_navi.get_navigation_links_text()
        expected_link = homepage_navi.NAVI_LINKS_TEXT
        assert expected_link == actual_link, 'Verifying header navigation links text...'
        elements1 = homepage_navi.get_navig_links()
        for index in range(13):
            homepage_navi.get_navig_links()[index].click()
            homepage_navi.driver.delete_all_cookies()
            time.sleep(5)
