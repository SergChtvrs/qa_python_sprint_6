import allure
from pages.base_page import BasePage
from locators.transition_page_locators import TransitionPageLocators


class TransitionPage(BasePage):
    @allure.step('Переходим на главную страницу')
    def switch_to_scooter_page(self):
        self.click_to_element(TransitionPageLocators.SCOOTER_LOGO_LOCATOR)

    @allure.step('Переходим на страницу Дзена')
    def switch_to_dzen_page(self):
        self.click_to_element(TransitionPageLocators.DZEN_LOGO_LOCATOR)
        self.switch_to_window_with_waiting()

    @allure.step('Получаем текст заголовка главной страницы')
    def get_scooter_headline_text(self):
        return self.get_text_from_element(TransitionPageLocators.SCOOTER_MAIN_TEXT_LOCATOR)

    @allure.step('Находим логотип на странице Дзена')
    def check_dzen_button(self):
        return self.find_element_with_waiting(TransitionPageLocators.DZEN_LOGO_LINK_LOCATOR)
