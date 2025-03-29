import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import requests
from random_data import *
import allure
from url import Url
from data import IngredientData


@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    if driver_class == webdriver.Chrome:
        options = Options()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get(Url.base_url)
        yield driver
        driver.quit()
    elif driver_class == webdriver.Firefox:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(Url.base_url)
        yield driver
        driver.quit()


@pytest.fixture
def get_random_user():
    email = get_random_email()
    password = get_random_password()
    name = get_random_name()
    return email, password, name


@pytest.fixture
@allure.title('Создание рандомного пользователя и его удаление')
def create_user_and_delete():
    payload_cred = {
        'email': get_random_email(),
        'password': get_random_password(),
        'name': get_random_name()
    }
    response = requests.post(Url.register_user, data=payload_cred)
    response_body = response.json()
    yield payload_cred, response_body
    access_token = response_body['accessToken']
    requests.delete(Url.delete_user, headers={'Authorization': access_token})



@pytest.fixture
@allure.title('Токены созданного пользователя')
def set_user_tokens(driver, create_user_and_delete):
    driver.get(Url.base_url)
    user_data = create_user_and_delete[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')


@pytest.fixture
@allure.title('Создание рандомного пользователя и заказа')
def create_user_and_order(create_user_and_delete):
    access_token = create_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [IngredientData.burger]}
    response_body = requests.post(Url.get_order, data=payload, headers=headers)
    yield access_token, response_body
    requests.delete(Url.delete_user, headers={'Authorization': access_token})
