import allure

from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage

class TestScooterOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Заказ самоката с использованием кнопки "Заказать" в верхней части страницы')  # декораторы
    @allure.description('Позитивный сценарий заказа самоката с использованием кнопки "Заказать" в верхней части страницы')
    def test_order_button_at_page_top(self):
        arendator = {'Имя': 'Василий', 'Фамилия': 'Иванов', 'Адрес': 'Москва, ул. Ольховская, 14, стр. 1',
                     'Станция': 'Бульвар Рокоссовского', 'Телефон': '89108494395',
                     'Когда привезти': 'Choose среда, 18-е октября 2023 г.', 'Срок аренды': 'сутки',
                     'Цвет самоката': 'чёрный жемчуг', 'Комментарий для курьера': 'Код домофона: 1234'}

        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)

        base_page.check_button_order_in_top_page_is_visible()
        base_page.click_button_order_in_top_page()

        order_page = OrderPage(self.driver)

        order_page.check_order_first_page_is_opened()

        order_page.enter_data_to_inputs_on_first_order_page(arendator)
        order_page.click_button_next()

        order_page.check_order_second_page_is_opened()

        order_page.enter_data_to_inputs_on_second_order_page(arendator)
        order_page.click_button_order()

        order_page.check_modal_window_is_opened()

        order_page.click_button_yes()

    @allure.title('Заказ самоката с использованием кнопки "Заказать" в нижней части страницы')  # декораторы
    @allure.description('Позитивный сценарий заказа самоката с использованием кнопки "Заказать" в нижней части страницы')
    def test_order_button_at_page_bottom(self):
        arendator = {'Имя': 'Петр', 'Фамилия': 'Сидоров', 'Адрес': 'Москва, ул. Ольховская, 24, стр. 2',
                     'Станция': 'Бульвар Рокоссовского', 'Телефон': '89108494323',
                     'Когда привезти': 'Choose среда, 18-е октября 2023 г.', 'Срок аренды': 'сутки',
                     'Цвет самоката': 'чёрный жемчуг', 'Комментарий для курьера': 'Код домофона: 5678'}

        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        base_page = BasePage(self.driver)

        base_page.check_button_order_in_top_page_is_visible()
        base_page.click_button_order_in_bottom_page()

        order_page = OrderPage(self.driver)

        order_page.check_order_first_page_is_opened()

        order_page.enter_data_to_inputs_on_first_order_page(arendator)
        order_page.click_button_next()

        order_page.check_order_second_page_is_opened()

        order_page.enter_data_to_inputs_on_second_order_page(arendator)
        order_page.click_button_order()

        order_page.check_modal_window_is_opened()

        order_page.click_button_yes()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
