from page_objects.page_base import PageBase
from locators.locators_page_account import LocatorsAccount
import allure


class PageAccount(PageBase):
    @allure.step('Клик по кнопке "История заказов"')
    def click_order_history_button(self):
        self.click_on_element(LocatorsAccount.history_orders)

    @allure.step('Отображение описания раздела')
    def check_displaying_of_description(self):
        return self.check_displayed_element(LocatorsAccount.description)

    @allure.step('Клик по кнопке "Выйти"')
    def click_logout_button(self):
        self.click_on_element(LocatorsAccount.button_logout)

    @allure.step('Загрузка кнопки "Зарегистрироваться"')
    def wait_visibility_button_register(self):
        self.wait_visibility_of_element(LocatorsAccount.button_register)

    @allure.step('Отображение кнопки "Зарегистрироваться"')
    def check_displayed_button_register(self):
        return self.check_displayed_element(LocatorsAccount.button_register)

    @allure.step('Загрузка текста описания раздела')
    def wait_visibility_description(self):
        self.wait_visibility_of_element(LocatorsAccount.description)
