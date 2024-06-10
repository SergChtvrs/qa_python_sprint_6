from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCORDION_QUESTION = By.ID, 'accordion__heading-{}'  # локатор вопросов
    ACCORDION_ANSWER = By.XPATH, '//*[@id="accordion__panel-{}"]/p'  # локатор ответов
    ORDER_BUTTON_HEADER = (By.XPATH,
                           '//*[contains(@class, "Header_Nav")]/*[contains(@class, "Button_Button")]')  # кнопка Заказать в шапке
    ORDER_BUTTON_LANDING = (By.XPATH,
                            '//*[contains(@class, "Home_FinishButton")]/*[contains(@class, "Button_Button")]')  # кнопка Заказать на странице лендинга
    COOKIES_BUTTON = By.ID, 'rcc-confirm-button'  # кнопка подтверждения cookies
