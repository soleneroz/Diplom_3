from page_objects.page_base import PageBase
from locators.locators_page_order_feed import LocatorsPageOrderFeed
import allure


class PageFeed(PageBase):

    @allure.step('Кликнуть по первому или последнему заказу в ленте')
    def click_order_card(self):
        self.wait_visibility_of_element(LocatorsPageOrderFeed.order_in_feed)
        self.click_on_element(LocatorsPageOrderFeed.order_in_feed)

    @allure.step('Узнать наличие номера заказа в ленте заказов')
    def check_id_order_feed(self, order_id):
        locator = LocatorsPageOrderFeed.id_order_card_in_feed_with_substitutions
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_wait(locator_with_order_id)
        return self.check_displayed_element(locator_with_order_id)

    @allure.step('Узнать количество заказов за всё время')
    def get_quantity_orders(self):
        self.find_element_wait(LocatorsPageOrderFeed.quantity_orders)
        return self.get_text_element(LocatorsPageOrderFeed.quantity_orders)

    @allure.step('Текст заголовка раздела заказов')
    def get_text_on_title_orders_list(self):
        return self.get_text_element(LocatorsPageOrderFeed.title_orders_feed)

    @allure.step('Текст заголовка модального окна с деталями заказа')
    def get_text_on_title_modal_window_order(self):
        return self.get_text_element(LocatorsPageOrderFeed.title_modal_window_order)

    @allure.step('Узнать номер последнего заказа в разделе "В работе"')
    def get_order_num_feed_progress_section(self):
        return self.get_text_element(LocatorsPageOrderFeed.num_of_order_in_progress)

    @allure.step('Узнать количество заказов за сегодня')
    def get_daily_quantity_orders(self):
        self.find_element_wait(LocatorsPageOrderFeed.daily_quantity_orders)
        return self.get_text_element(LocatorsPageOrderFeed.daily_quantity_orders)
