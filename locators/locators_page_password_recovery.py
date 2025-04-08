from selenium.webdriver.common.by import By


class LocatorsPagePasswordRecovery:

    button_recovery = (By.CLASS_NAME, 'button_button__33qZ0')
    button_forget_password = By.XPATH, '//a[text() = "Восстановить пароль"]'
    password_input = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    email_input = (By.CLASS_NAME, 'input__textfield')
    value_password_is_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]')
    value_password_is_invisible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_type_password")]')
    eye_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
