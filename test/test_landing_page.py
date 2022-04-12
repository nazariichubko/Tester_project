import time
import pytest
from pom.home_page_nav import HomePageNavigation


@pytest.mark.usefixtures('test_setup')
class TestLandingPage:

    def test_navi_links(self):
        homepage_navi = HomePageNavigation(self.driver)
        for index in range(13):
            homepage_navi.get_navig_links()[index].click()
            time.sleep(1.5)
