import pytest
from selenium import webdriver
from helpers import customer_generator
from helpers import rent_date_generator
from helpers import about_generator
from data import Consts


@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(Consts.link)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def customer():
    customer = customer_generator()
    return customer


@pytest.fixture(scope='function')
def rent_date():
    rent_date = rent_date_generator()
    return rent_date


@pytest.fixture(scope='function')
def about_data():
    about_data = about_generator()
    return about_data
