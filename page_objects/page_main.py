from page_objects.page_base import PageBase
from locators.locators_page_main import LocatorsPageMain
import allure


class PageMain(PageBase):

    @allure.step('Получение заголовка конструктора')
    def get_text_title_constructor(self):
        return self.get_text_element(LocatorsPageMain.constructor_title)

    @allure.step('На главной странице клик по кнопке "Войти в аккаунт"')
    def click_button_login_main(self):
        self.click_on_element(LocatorsPageMain.button_login_main)

    @allure.step('В хедере клик по кнопке "Лента заказов"')
    def click_header_feed_button(self):
        self.wait_visibility_of_element(LocatorsPageMain.button_order_feed_header)
        self.click_on_element(LocatorsPageMain.button_order_feed_header)

    @allure.step('В хедере клик по кнопке перехода в ЛК')
    def click_personal_account_in_header(self):
        self.wait_visibility_of_element(LocatorsPageMain.button_personal_account)
        self.click_on_element(LocatorsPageMain.button_personal_account)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displayed_confirm_modal_window_order(self):
        self.wait_visibility_of_element(LocatorsPageMain.confirmation_modal_window_of_order)
        return self.check_displayed_element(LocatorsPageMain.confirmation_modal_window_of_order)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.wait_visibility_of_element(LocatorsPageMain.ingredient)
        self.click_on_element(LocatorsPageMain.ingredient)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displayed_modal_window_details(self):
        self.wait_visibility_of_element(LocatorsPageMain.header_modal_window_details)
        return self.check_displayed_element(LocatorsPageMain.header_modal_window_details)

    @allure.step('Переход на страницу конструктора')
    def click_button_constructor(self):
        self.wait_visibility_of_element(LocatorsPageMain.header_page_constructor)
        self.click_on_element(LocatorsPageMain.header_page_constructor)

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_order_in_modal_window_confirm(self):
        self.wait_element_change_text(LocatorsPageMain.num_order_in_modal_window_confirm, '9999')
        return self.get_text_element(LocatorsPageMain.num_order_in_modal_window_confirm)

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_modal_window(self):
        self.wait_visibility_of_element(LocatorsPageMain.button_close_modal_window)
        self.click_on_element(LocatorsPageMain.button_close_modal_window)

    @allure.step('Добавить интгридиенты')
    def drag_and_drop_ingredient_order(self):
        source_element = self.find_element_wait(LocatorsPageMain.burger_ingredient)
        target_element = self.find_element_wait(LocatorsPageMain.place_for_ingredients)
        self.drag_drop_element(source_element, target_element)

    @allure.step('Проверить отсутствие отображения окна "Детали ингредиента"')
    def check_not_displayed_modal_window_details(self):
        self.wait_close_element(LocatorsPageMain.header_modal_window_details)
        if not self.check_displayed_element(LocatorsPageMain.header_modal_window_details):
            return True

    @allure.step('Получить количество ингредиентов')
    def get_count_ingredients(self):
        return self.get_text_element(LocatorsPageMain.count_ingredient)

    @allure.step('Клик по кнопке закрытия окна создания заказа')
    def click_button_close_confirm_modal_window(self):
        self.check_element_is_click(LocatorsPageMain.button_close_confirm)
        self.click_on_element(LocatorsPageMain.button_close_confirm)

    @allure.step('Клик по кнопкк создания заказа')
    def click_button_make_order(self):
        self.click_on_element(LocatorsPageMain.button_make_order)
