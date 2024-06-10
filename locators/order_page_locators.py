from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат":
    NAME_LOCATOR = By.XPATH, '//input[@placeholder="* Имя"]'  # поле Имя
    LAST_NAME_LOCATOR = By.XPATH, '//input[@placeholder="* Фамилия"]'  # поле Фамилия
    ADDRESS_LOCATOR = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'  # поле Адресс
    METRO_LOCATOR = By.XPATH, '//input[@placeholder="* Станция метро"]'  # поле Метро
    METRO_LIST_ELM_LOCATOR = By.XPATH, '//*[contains(@class, "Order_Text") and text()="{}"]'  # элемент списка метро
    MOBILE_LOCATOR = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'  # поле Телефон
    NEXT_BUTTON_LOCATOR = (By.XPATH,
                           '//*[contains(@class, "Order_NextButton")]/*[contains(@class, "Button_Button")]')  # кнопка Далее
    # Форма "Про аренду":
    DATE_RENT_LOCATOR = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'  # поле Когда привезти
    DATE_FROM_CALENDAR_LOCATOR = (By.XPATH,
                                  '//*[contains(@class, "datepicker__day") and text()="{}"]')  # дата в календаре поля Когда привезти
    RENTAL_PERIOD_LOCATOR = By.XPATH, '//*[@class="Dropdown-placeholder"and text()="* Срок аренды"]'  # Срок аренды
    RENTAL_PERIOD_LIST_ELM_LOCATOR = By.XPATH, '//*[@class ="Dropdown-option" and text()="{}"]'  # элемент списка срока аренды
    COLOUR_LOCATOR = By.ID, '{}'   # чекбоксы цвета
    COMMENT_LOCATOR = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'  # поле Комментарий
    ORDER_BUTTON_LOCATOR = By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Заказать"]'  # кнопка Заказать
    # Модальные окна
    YES_BUTTON = By.XPATH, '//*[contains(@class,"Order_Modal")]//*[text()="Да"]'  # кнопка Да
    CONFIRMATION_SUCCESS_TEXT_LOCATOR = By.XPATH, '//*[contains(@class, "Order_ModalHeader")]'  # локатор текста Заказ оформлен
