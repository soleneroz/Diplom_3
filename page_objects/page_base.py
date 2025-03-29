from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загрузка элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ввести значение в инпут')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Найти элемент')
    def find_element_wait(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Перенести элемент')
    def drag_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).pause(5).perform()

    @allure.step('Получить текст на элементе')
    def get_text_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Закрытие элемента')
    def wait_close_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверить доступность элемента для клика')
    def check_element_is_click(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Проверить отображение элемента')
    def check_displayed_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать смену текста')
    def wait_element_change_text(self, locator, value):
        return WebDriverWait(self.driver, 15).until_not(expected_conditions.text_to_be_present_in_element(locator, value))

    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        target = self.check_element_is_click(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()
