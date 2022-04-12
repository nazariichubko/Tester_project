import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_options


@pytest.fixture
def get_chr_options():
    options1 = chr_options()
    options1.add_argument('chrome') # 'headless' parameter allow to execute tests without runinng Browser UI.
    options1.add_argument('--start-maximized')
    options1.add_argument("--window-size=1366,768")
    return options1

@pytest.fixture
def get_wbdriver(get_chr_options):
    options1 = get_chr_options
    driver = webdriver.Chrome(options=options1, executable_path=r"C:\Users\nazar\git\Tester_project\test\chromedriver.exe")
    return driver

@pytest.fixture(scope='function') # if scope argument =  'session' test will be executed in single browser window at a teime
def test_setup(request, get_wbdriver):
    driver = get_wbdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()