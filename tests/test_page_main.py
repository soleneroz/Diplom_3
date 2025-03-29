from page_objects.page_main import PageMain
from page_objects.page_order_feed import PageFeed
import allure


class TestMainPage:

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_making_order_by_authenticated_user_success(self, driver, set_user_tokens):
        page_main = PageMain(driver)
        page_main.click_button_login_main()
        page_main.drag_and_drop_ingredient_order()
        page_main.click_button_make_order()
        assert page_main.check_displayed_confirm_modal_window_order()
    @allure.title('Клик по кнопке "Конструктор" и проверка перехода')
    def test_navigate_to_constructor_success(self, driver):
        page_main = PageMain(driver)
        page_main.click_header_feed_button()
        page_main.click_button_constructor()
        assert 'Соберите бургер' in page_main.get_text_title_constructor()

    @allure.title('Клик по кнопке "Лента заказов" и проверка перехода')
    def test_navigate_to_order_history_success(self, driver):
        page_main = PageMain(driver)
        page_feed = PageFeed(driver)
        page_main.click_header_feed_button()
        assert page_feed.get_text_on_title_orders_list() == 'Лента заказов'

    @allure.title('Проверка отображения окна "Детали ингридиента"')
    def test_displaying_modal_window_details_of_ingredient_success(self, driver):
        page_main = PageMain(driver)
        page_main.click_ingredient()
        assert page_main.check_displayed_modal_window_details()

    @allure.title('Проверка закрытия окна "Детали ингредиента" при клике на крестик')
    def test_close_modal_window_details_of_ingredient_success(self, driver):
        page_main = PageMain(driver)
        page_main.click_ingredient()
        page_main.close_modal_window()
        assert page_main.check_not_displayed_modal_window_details()

    @allure.title('Увеличения числа на счетчике после добавления ингредиента в заказ')
    def test_changing_counter_for_ingredients_in_order_success(self, driver):
        page_main = PageMain(driver)
        page_main.drag_and_drop_ingredient_order()
        assert page_main.get_count_ingredients() == '2'
