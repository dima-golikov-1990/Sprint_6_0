import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators

class OrderPage:
    scooter_for_who_text = OrderPageLocators.scooter_for_who_text

    input_name = OrderPageLocators.input_name
    input_surname = OrderPageLocators.input_surname
    input_address = OrderPageLocators.input_address
    input_station = OrderPageLocators.input_station
    input_phone = OrderPageLocators.input_phone

    button_next = OrderPageLocators.button_next
    arenda_text = OrderPageLocators.arenda_text

    input_when = OrderPageLocators.input_when
    input_period = OrderPageLocators.input_period
    input_comment = OrderPageLocators.input_comment

    want_to_place_order_text = OrderPageLocators.want_to_place_order_text

    button_order = OrderPageLocators.button_order
    button_yes = OrderPageLocators.button_yes

    def __init__(self, driver):
        self.driver = driver

    @allure.step('проверить, что первая страница оформления заказа открылась')
    def check_order_first_page_is_opened(self):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((self.scooter_for_who_text)))

    @allure.step('заполнить данные на первой странице оформления заказа')
    def enter_data_to_inputs_on_first_order_page(self, arendator):
        self.driver.find_element(*self.input_name).send_keys(arendator['Имя'])
        self.driver.find_element(*self.input_surname).send_keys(arendator['Фамилия'])
        self.driver.find_element(*self.input_address).send_keys(arendator['Адрес'])

        self.driver.find_element(*self.input_station).click()
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='" + arendator['Станция'] + "']")))
        self.driver.find_element(By.XPATH, "//*[text()='" + arendator['Станция'] + "']").click()

        self.driver.find_element(*self.input_phone).send_keys(arendator['Телефон'])

    @allure.step('нажать кнопку "Далее"')
    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()

    @allure.step('проверить, что вторая страница оформления заказа открылась')
    def check_order_second_page_is_opened(self):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((self.arenda_text)))

    @allure.step('заполнить данные на второй странице оформления заказа')
    def enter_data_to_inputs_on_second_order_page(self, arendator):
        self.driver.find_element(*self.input_when).click()
        self.driver.find_element(By.XPATH, "//div[@aria-label='" + arendator['Когда привезти'] + "']").click()

        self.driver.find_element(*self.input_period).click()
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='" + arendator['Срок аренды'] + "']")))
        self.driver.find_element(By.XPATH, "//*[text()='" + arendator['Срок аренды'] + "']").click()

        self.driver.find_element(By.XPATH, "//label[text()='" + arendator['Цвет самоката'] + "']").click()

        self.driver.find_element(*self.input_comment).send_keys(arendator['Комментарий для курьера'])

    @allure.step('нажать кнопку "Заказать" на второй странице оформления заказа')
    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()

    @allure.step('провериь, что открылось модальное окно для подтверждения заказа')
    def check_modal_window_is_opened(self):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((self.want_to_place_order_text)))

    @allure.step('нажать кнопку "Да" в модальном окне')
    def click_button_yes(self):
        self.driver.find_element(*self.button_yes).click()