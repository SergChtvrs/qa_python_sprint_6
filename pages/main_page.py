import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from helpers import format_locators


class MainPage(BasePage):
    @allure.step('Принимаем куки')
    def cookies_acceptation(self):
        self.click_to_element(MainPageLocators.COOKIES_BUTTON)

    @allure.step('получаем текст ответа')
    def get_answer_text(self, num):
        answer_locator = format_locators(MainPageLocators.ACCORDION_ANSWER, num)
        question_locator = format_locators(MainPageLocators.ACCORDION_QUESTION, num)
        self.scroll_to_element(question_locator)
        self.click_to_element(question_locator)
        return self.get_text_from_element(answer_locator)

    @allure.step('Жмем на кнопку Заказать')
    def make_order(self, button):
        self.click_to_element(button)
