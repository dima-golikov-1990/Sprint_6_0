import allure
from order_scooter_page import OrderScooterPage

class TestOrderScooterPage:
    @allure.title('Заказ самоката с использованием кнопки "Заказать" в верхней части страницы')  # декораторы
    @allure.description('Позитивный сценарий заказа самоката с использованием кнопки "Заказать" в верхней части страницы')
    def test_order_button_at_page_top(self, driver):
        arendator = {'Имя': 'Василий', 'Фамилия': 'Иванов', 'Адрес': 'Москва, ул. Ольховская, 14, стр. 1',
                     'Станция': 'Бульвар Рокоссовского', 'Телефон': '89108494395',
                     'Когда привезти': 'Choose среда, 18-е октября 2023 г.', 'Срок аренды': 'сутки',
                     'Цвет самоката': 'чёрный жемчуг', 'Комментарий для курьера': 'Код домофона: 1234'}

        OrderScooterPage.click_button_order_at_page_top(self, driver)

        OrderScooterPage.complete_data_on_order_first_page(self, driver, arendator)
        OrderScooterPage.complete_data_on_order_second_page(self, driver, arendator)

        OrderScooterPage.cancel_order(self, driver)

        OrderScooterPage.click_to_scooter_logo(self, driver)

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        OrderScooterPage.click_to_yandex_logo(self, driver)

        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Заказ самоката с использованием кнопки "Заказать" в нижней части страницы')  # декораторы
    @allure.description('Позитивный сценарий заказа самоката с использованием кнопки "Заказать" в нижней части страницы')
    def test_order_button_at_page_bottom(self, driver):
        arendator = {'Имя': 'Петр', 'Фамилия': 'Сидоров', 'Адрес': 'Москва, ул. Ольховская, 24, стр. 2',
                     'Станция': 'Бульвар Рокоссовского', 'Телефон': '89108494323',
                     'Когда привезти': 'Choose среда, 18-е октября 2023 г.', 'Срок аренды': 'сутки',
                     'Цвет самоката': 'чёрный жемчуг', 'Комментарий для курьера': 'Код домофона: 5678'}

        OrderScooterPage.click_button_order_at_page_bottom(self, driver)

        OrderScooterPage.complete_data_on_order_first_page(self, driver, arendator)
        OrderScooterPage.complete_data_on_order_second_page(self, driver, arendator)

        OrderScooterPage.cancel_order(self, driver)

        OrderScooterPage.click_to_scooter_logo(self, driver)

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        OrderScooterPage.click_to_yandex_logo(self, driver)

        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
















