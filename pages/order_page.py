import allure
from pages.base_page import BasePage
from helpers import format_locators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_for_whom_form(self, name, last_name, address, metro, mobile):
        self.insert_text_to_element(OrderPageLocators.NAME_LOCATOR, name)
        self.insert_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, last_name)
        self.insert_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, address)
        self.insert_text_to_element(OrderPageLocators.METRO_LOCATOR, metro)
        station_locator = format_locators(OrderPageLocators.METRO_LIST_ELM_LOCATOR, metro)
        self.click_to_element(station_locator)
        self.insert_text_to_element(OrderPageLocators.MOBILE_LOCATOR, mobile)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)

    @allure.step('Заполняем форму "Об аренде"')
    def fill_about_rent_form(self, rent_date, period, colour, comment):
        self.insert_text_to_element(OrderPageLocators.DATE_RENT_LOCATOR, rent_date['date'])
        rental_date = format_locators(OrderPageLocators.DATE_FROM_CALENDAR_LOCATOR, rent_date['day'])
        self.click_to_element(rental_date)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_LOCATOR)
        rental_period = format_locators(OrderPageLocators.RENTAL_PERIOD_LIST_ELM_LOCATOR, period)
        self.click_to_element(rental_period)
        scooter_colour = format_locators(OrderPageLocators.COLOUR_LOCATOR, colour)
        self.click_to_element(scooter_colour)
        self.insert_text_to_element(OrderPageLocators.COMMENT_LOCATOR, comment)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_LOCATOR)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Получаем текст об успешном оформлении заказа')
    def check_order_success(self):
        return self.get_text_from_element(OrderPageLocators.CONFIRMATION_SUCCESS_TEXT_LOCATOR)

