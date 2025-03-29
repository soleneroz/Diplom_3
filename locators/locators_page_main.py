from selenium.webdriver.common.by import By


class LocatorsPageMain:

    button_login_main = By.XPATH, './/button[text() = "Войти в аккаунт"]'
    button_order_feed_header = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    header_page_constructor = (By.XPATH, '//p[text() = "Конструктор"]')
    constructor_title = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    ingredient = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')
    header_modal_window_details = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')
    button_close_modal_window = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')
    place_for_ingredients = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    button_make_order = (By.CLASS_NAME, 'button_button__33qZ0')
    count_ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[@class="counter_counter__num__3nue1"][1]')
    confirmation_modal_window_of_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains(@class, "Modal_modal__container")]')
    num_order_in_modal_window_confirm = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
    button_close_confirm = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    burger_ingredient = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    buns_block = (By.XPATH, '//span[text() = "Булки"]')
