import allure
from pages.transition_page import TransitionPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestTransitionPage:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_transition_from_order_page_to_main_page(self, driver,):
        transition_page = TransitionPage(driver)
        main_page = MainPage(driver)
        main_page.cookies_acceptation()
        main_page.make_order(MainPageLocators.ORDER_BUTTON_HEADER)
        transition_page.switch_to_scooter_page()
        assert 'Самокат' in transition_page.get_scooter_headline_text()

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_transition_from_order_page_to_dzen(self, driver):
        transition_page = TransitionPage(driver)
        main_page = MainPage(driver)
        main_page.cookies_acceptation()
        transition_page.switch_to_dzen_page()
        assert transition_page.check_dzen_button()

