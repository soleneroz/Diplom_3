from page_objects.page_order_feed import PageFeed
from page_objects.page_main import PageMain
from page_objects.page_history_order import PageHistoryOrder
from page_objects.page_account import PageAccount
from conftest import *
import allure


class TestFeedPage:

    @allure.title('Отображение заказа из истории пользователя в ленте')
    def test_displayed_feed_new_order_from_history(self, driver, create_user_and_order, set_user_tokens):
        page_main = PageMain(driver)
        page_account = PageAccount(driver)
        page_history_order = PageHistoryOrder(driver)
        page_feed = PageFeed(driver)
        page_main.click_personal_account_in_header()
        page_account.click_order_history_button()
        order_id = page_history_order.get_id_order_card()
        page_main.click_header_feed_button()
        assert page_feed.check_id_order_feed(order_id)

    @allure.title('При клике на заказ открытие всплывающего окна с деталями')
    def test_displayed_modal_window_order_details(self, driver):
        page_main = PageMain(driver)
        page_feed = PageFeed(driver)
        page_main.click_header_feed_button()
        page_feed.click_order_card()
        assert 'бургер' in page_feed.get_text_on_title_modal_window_order()

    @allure.title('Увеличение числа ежедневных выполненных заказов')
    def test_change_counter_daily_quantity_orders(self, driver, set_user_tokens):
        page_main = PageMain(driver)
        page_feed = PageFeed(driver)
        page_main.click_button_login_main()
        page_main.click_header_feed_button()
        orders_count_1 = page_feed.get_daily_quantity_orders()
        page_main.click_button_constructor()
        page_main.drag_and_drop_ingredient_order()
        page_main.click_button_make_order()
        page_main.click_button_close_confirm_modal_window()
        page_main.click_header_feed_button()
        orders_count_2 = page_feed.get_daily_quantity_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Увеличение числа общего количества выполненных заказов')
    def test_change_counter_quantity_orders(self, driver, set_user_tokens):
        page_main = PageMain(driver)
        page_feed = PageFeed(driver)
        page_main.click_header_feed_button()
        orders_count_1 = page_feed.get_quantity_orders()
        page_main.click_button_constructor()
        page_main.click_button_login_main()
        page_main.drag_and_drop_ingredient_order()
        page_main.click_button_make_order()
        page_main.click_button_close_confirm_modal_window()
        page_main.click_header_feed_button()
        orders_count_2 = page_feed.get_quantity_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('В разделе "В работе" появление нового заказа')
    def test_displayed_new_order_in_progress_feed(self, driver, set_user_tokens):
        page_main = PageMain(driver)
        page_feed = PageFeed(driver)
        page_main.click_button_login_main()
        page_main.drag_and_drop_ingredient_order()
        page_main.click_button_make_order()
        new_order_id = page_main.get_number_order_in_modal_window_confirm()
        page_main.click_button_close_confirm_modal_window()
        page_main.click_header_feed_button()
        assert page_feed.get_order_num_feed_progress_section() == '0' + new_order_id
