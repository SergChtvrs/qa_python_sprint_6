import allure
import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestOrderPage:
    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize('button',
                             [MainPageLocators.ORDER_BUTTON_HEADER,
                              MainPageLocators.ORDER_BUTTON_LANDING],
                             ids=['Оформление заказа через кнопку в шапке',
                                  'Оформление заказа через кнопку в лендинге'])
    def test_order(self, driver, button, customer, rent_date, about_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.cookies_acceptation()
        main_page.make_order(button)
        order_page.fill_for_whom_form(name=customer['name'],
                                      last_name=customer['last_name'],
                                      address=customer['address'],
                                      metro=customer['metro'],
                                      mobile=customer['mobile'])
        order_page.fill_about_rent_form(rent_date,
                                        period=about_data['period'],
                                        colour=about_data['colour'],
                                        comment=about_data['comment'])
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.check_order_success(), 'Teкст не сооответствует ожидаемому'
