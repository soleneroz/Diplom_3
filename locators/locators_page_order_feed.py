from selenium.webdriver.common.by import By


class LocatorsPageOrderFeed:

    title_orders_feed = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    order_in_feed = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    title_modal_window_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]//h2')
    section_orders_list = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')
    quantity_orders = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    modal_window_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]')
    id_order_card_in_feed_with_substitutions = (By.XPATH, './/*[text()="{order_id}"]')
    daily_quantity_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    num_of_order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]')
