from selenium.webdriver.common.by import By


class TransitionPageLocators:
    SCOOTER_LOGO_LOCATOR = By.XPATH, '//*[contains(@class, "Header_LogoScooter")]'  # логотип Самокат в шапке
    DZEN_LOGO_LOCATOR = By.XPATH, '//*[contains(@class, "Header_LogoYandex")]'  # логотип Дзен в шапке
    SCOOTER_MAIN_TEXT_LOCATOR = By.XPATH, '//*[contains(@class, "Home_Header")]'  # текст Заголовка на главной странице Самоката
    DZEN_LOGO_LINK_LOCATOR = By.XPATH, '//*[contains(@class, "ogoLink")]'  # кнопка геолокации на странице Дзена
