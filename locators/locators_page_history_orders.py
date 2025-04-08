from selenium.webdriver.common.by import By


class LocatorsPageHistoryOrders:

    card_order_title = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    card_order_id = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text_type_digits-default")])[1]')
    card_order = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
