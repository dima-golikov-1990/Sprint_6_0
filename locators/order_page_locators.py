from selenium.webdriver.common.by import By

class OrderPageLocators:
    scooter_for_who_text = [By.XPATH, "//*[text()='Для кого самокат']"]

    input_name = [By.XPATH, "//input[contains(@placeholder, 'Имя')]"] # поле "Имя"
    input_surname = [By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"] # поле "Фамилия"
    input_address = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"] # поле "Адрес"
    input_station = [By.XPATH, "//input[contains(@placeholder, 'Станция')]"] # поле "Станция"
    input_phone = [By.XPATH, "//input[contains(@placeholder, 'Телефон')]"] # поле "Телефон"

    button_next = [By.XPATH, "//button[text()='Далее']"] # поле "Далее"
    arenda_text = [By.XPATH, "//*[text()='Про аренду']"] # заголовок страницы "Про аренду"

    input_when = [By.XPATH, "//input[contains(@placeholder, 'Когда')]"] # поле "Когда"
    input_period = [By.CLASS_NAME, "Dropdown-placeholder"] # поле "Период"
    input_comment = [By.XPATH, "//input[contains(@placeholder, 'Комментарий')]"] # поле "Комментарий"

    want_to_place_order_text = [By.XPATH, "//*[text()='Хотите оформить заказ?']"] # заголовок модального окна "Хотите оформить заказ?"

    button_order = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    button_yes = [By.XPATH, "//button[text()='Да']"] # кнопка "Да"