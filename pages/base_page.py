from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def find_element_with_waiting(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_text_from_element(self, locator):
        return self.find_element_with_waiting(locator).text

    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def insert_text_to_element(self, locator, text):
        self.find_element_with_waiting(locator).send_keys(text)

    def switch_to_window_with_waiting(self):
        self.driver.switch_to.window(self.driver.window_handles[1])