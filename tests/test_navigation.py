import allure

from selenium import webdriver
from pages.base_page import BasePage

class TestNavigation:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка навигации при нажатии на лого "Самокат"')  # декораторы
    @allure.description('Проверка перехода на главную страницу при нажатии на лого "Самокат"')
    def test_click_scooter_logo(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)

        base_page.check_scooter_logo_is_visible()

        base_page.click_scooter_logo()

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


    @allure.title('Проверка навигации при нажатии на лого "Яндекс"')  # декораторы
    @allure.description('Проверка перехода на страницу "Яндекс.Дзен" при нажатии на лого "Яндекс"')
    def test_click_yandex_logo(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)

        base_page.check_yandex_logo_is_visible()

        base_page.click_yandex_logo()

        base_page.switch_to_second_tab_in_browser()

        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()