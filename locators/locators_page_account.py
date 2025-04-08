from selenium.webdriver.common.by import By


class LocatorsAccount:

    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'
    profile = (By.XPATH, '//a[@href = "/account/profile"]')
    button_logout = (By.XPATH, '//button[@type = "button"]')
    history_orders = (By.XPATH, '//a[@href = "/account/order-history"]')
    description = (By.XPATH, '//p[contains(@class, "Account_text")]')
