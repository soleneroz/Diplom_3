from page_objects.page_account import PageAccount
from page_objects.page_main import PageMain
from page_objects.page_history_order import PageHistoryOrder
import allure


class TestPageAccount:
    @allure.title('В хедере клик по кнопке "Личный кабинет" и переход')
    def test_navigate_page_account(self, driver, set_user_tokens):
        page_main = PageMain(driver)
        page_account = PageAccount(driver)
        page_main.click_personal_account_in_header()
        page_account.wait_visibility_description()
        assert page_account.check_displaying_of_description() is True

    @allure.title('Клик по кнопке "История заказов" и переход')
    def test_navigate_page_history_order(self, driver, set_user_tokens, create_user_and_order):
        page_main = PageMain(driver)
        page_account = PageAccount(driver)
        page_history_order = PageHistoryOrder(driver)
        page_main.click_personal_account_in_header()
        page_account.wait_visibility_description()
        page_account.click_order_history_button()
        page_history_order.wait_visibility_order_card()
        assert 'бургер' in page_history_order.get_text_order_card_title()

    @allure.title('Клик по кнопке "Выйти" и проверка выхода')
    def test_logout_profile(self, driver, set_user_tokens):
        page_main = PageMain(driver)
        page_account = PageAccount(driver)
        page_main.click_personal_account_in_header()
        page_account.wait_visibility_description()
        page_account.click_logout_button()
        page_account.wait_visibility_button_register()
        assert page_account.check_displayed_button_register()
