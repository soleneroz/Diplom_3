from page_objects.page_base import PageBase
from locators.locators_page_password_recovery import LocatorsPagePasswordRecovery
from random_data import *
import allure


class PagePasswordRecovery(PageBase):
    @allure.step('Открыть страницу восстановления пароля')
    def navigate_page_recovery_password(self):
        self.wait_visibility_of_element(LocatorsPagePasswordRecovery.button_forget_password)
        self.click_on_element(LocatorsPagePasswordRecovery.button_forget_password)

    @allure.step('Отображение поля email')
    def check_displayed_input_email(self):
        return self.check_displayed_element(LocatorsPagePasswordRecovery.email_input)

    @allure.step('Отображение поля пароль')
    def check_displayed_input_password(self):
        self.wait_visibility_of_element(LocatorsPagePasswordRecovery.password_input)
        return self.check_displayed_element(LocatorsPagePasswordRecovery.password_input)

    @allure.step('Ввести email')
    def send_keys_email(self):
        self.wait_visibility_of_element(LocatorsPagePasswordRecovery.email_input)
        email = get_random_email()
        self.send_keys_to_input(LocatorsPagePasswordRecovery.email_input, email)

    @allure.step('Ввести пароль')
    def send_keys_password(self):
        self.wait_visibility_of_element(LocatorsPagePasswordRecovery.password_input)
        password = get_random_password()
        self.send_keys_to_input(LocatorsPagePasswordRecovery.password_input, password)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recovery_button(self):
        self.wait_visibility_of_element(LocatorsPagePasswordRecovery.button_recovery)
        self.click_on_element(LocatorsPagePasswordRecovery.button_recovery)

    @allure.step('Отсутствие отображения пароля')
    def check_not_displayed_password_value(self):
        return self.check_displayed_element(LocatorsPagePasswordRecovery.value_password_is_invisible)

    @allure.step('Отображение пароля')
    def check_displayed_password_value(self):
        return self.check_displayed_element(LocatorsPagePasswordRecovery.value_password_is_visible)

    @allure.step('Клик по иконке глаза в поле ввода пароля')
    def click_eye_icon(self):
        self.wait_visibility_of_element(LocatorsPagePasswordRecovery.eye_icon)
        self.click_on_element(LocatorsPagePasswordRecovery.eye_icon)
