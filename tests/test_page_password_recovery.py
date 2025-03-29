from page_objects.page_password_recovery import PagePasswordRecovery
from page_objects.page_main import PageMain
from conftest import *
import allure


class TestPasswdRecoveryPage:
    @allure.title('Переход на страницу восстановления пароля')
    def test_navigate_page_recovery_password(self, driver):
        page_main = PageMain(driver)
        page_main.click_button_login_main()
        page_recovery = PagePasswordRecovery(driver)
        page_recovery.navigate_page_recovery_password()
        assert page_recovery.check_displayed_input_email()

    @allure.title('Проверка маски пароля после кликов по иконке глаза')
    def test_double_click_on_eye_icon_makes_passwd_invisible_success(self, driver):
        page_main = PageMain(driver)
        page_main.click_button_login_main()
        page_recovery = PagePasswordRecovery(driver)
        page_recovery.navigate_page_recovery_password()
        page_recovery.send_keys_email()
        page_recovery.click_recovery_button()
        page_recovery.send_keys_password()
        page_recovery.click_eye_icon()
        page_recovery.click_eye_icon()
        assert page_recovery.check_not_displayed_password_value()

    @allure.title('Отображение пароля после клика на инконку глаза')
    def test_click_on_eye_icon_makes_passwd_visible_success(self, driver):
        page_main = PageMain(driver)
        page_main.click_button_login_main()
        page_recovery = PagePasswordRecovery(driver)
        page_recovery.navigate_page_recovery_password()
        page_recovery.send_keys_email()
        page_recovery.click_recovery_button()
        page_recovery.send_keys_password()
        page_recovery.click_eye_icon()
        assert page_recovery.check_displayed_password_value()

    @allure.title('Переход к восстановлению пароля при вводе email и клике по кнопке "Восстановить"')
    def test_click_recovery_button_success(self, driver):
        page_main = PageMain(driver)
        page_main.click_button_login_main()
        page_recovery = PagePasswordRecovery(driver)
        page_recovery.navigate_page_recovery_password()
        page_recovery.send_keys_email()
        page_recovery.click_recovery_button()
        assert page_recovery.check_displayed_input_password()
