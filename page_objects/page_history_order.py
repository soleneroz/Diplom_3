from locators.locators_page_history_orders import LocatorsPageHistoryOrders
from page_objects.page_base import PageBase
import allure


class PageHistoryOrder(PageBase):

    @allure.step('Узнать номер заказа в карточке')
    def get_id_order_card(self):
        return self.get_text_element(LocatorsPageHistoryOrders.card_order_id)

    @allure.step('Узнать текст карточки заказа')
    def get_text_order_card_title(self):
        return self.get_text_element(LocatorsPageHistoryOrders.card_order_title)

    @allure.step('Загрузка карточки заказа')
    def wait_visibility_order_card(self):
        self.wait_visibility_of_element(LocatorsPageHistoryOrders.card_order)
