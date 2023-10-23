from selenium.webdriver.common.by import By

class OrderScooterPageLocators:
    order_button = [By.XPATH, "//button[text()='Заказать']"]
    scooter_for_who_text = [By.XPATH, "//*[text()='Для кого самокат']"]

    input_name = [By.XPATH, "//input[contains(@placeholder, 'Имя')]"]
    input_surname = [By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"]
    input_address = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"]
    input_station = [By.XPATH, "//input[contains(@placeholder, 'Станция')]"]
    input_phone = [By.XPATH, "//input[contains(@placeholder, 'Телефон')]"]

    button_next = [By.XPATH, "//button[text()='Далее']"]
    arenda_text = [By.XPATH, "//*[text()='Про аренду']"]

    input_when = [By.XPATH, "//input[contains(@placeholder, 'Когда')]"]
    input_period = [By.CLASS_NAME, "Dropdown-placeholder"]
    input_comment = [By.XPATH, "//input[contains(@placeholder, 'Комментарий')]"]

    want_to_place_order_text = [By.XPATH, "//*[text()='Хотите оформить заказ?']"]
    cancel_button = [By.XPATH, "//button[text()='Нет']"]

    link_scooter_logo = [By.XPATH, "//a[@href='/']"]
    deliver_to_door_text = [By.XPATH, "//*[text()='Привезём его прямо к вашей двери,']"]

    link_yandex_logo = [By.XPATH, "//a[@href='//yandex.ru']"]