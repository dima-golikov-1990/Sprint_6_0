from selenium.webdriver.common.by import By

class BasePageLocators:
    order_button_in_top_page = [By.XPATH, "(//button[text()='Заказать'])[1]"] # кнопка "Заказать" в верхней части страницы
    order_button_in_bottom_page = [By.XPATH, "(//button[text()='Заказать'])[2]"]  # кнопка "Заказать" в нижней части страницы

    order_status_button = [By.XPATH, "//button[text()='Статус заказа']"] # кнопка "Статус заказа"

    link_scooter_logo = [By.XPATH, "//a[@href='/']"] # лого "Самокат"
    link_yandex_logo = [By.XPATH, "//a[@href='//yandex.ru']"] # лого "Яндекс"