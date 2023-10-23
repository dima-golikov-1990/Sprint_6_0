from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from order_scooter_page_locators import OrderScooterPageLocators

class OrderScooterPage:
    def click_button_order_at_page_top(self, driver):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((OrderScooterPageLocators.order_button)))

        driver.find_element(*OrderScooterPageLocators.order_button).click()

    def click_button_order_at_page_bottom(self, driver):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((OrderScooterPageLocators.order_button)))

        order_button = driver.find_elements(*OrderScooterPageLocators.order_button)[1]
        driver.execute_script("arguments[0].scrollIntoView();", order_button)
        order_button.click()

    def complete_data_on_order_first_page(self, driver, arendator):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((OrderScooterPageLocators.scooter_for_who_text)))

        driver.find_element(*OrderScooterPageLocators.input_name).send_keys(arendator['Имя'])
        driver.find_element(*OrderScooterPageLocators.input_surname).send_keys(arendator['Фамилия'])
        driver.find_element(*OrderScooterPageLocators.input_address).send_keys(arendator['Адрес'])

        driver.find_element(*OrderScooterPageLocators.input_station).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='" + arendator['Станция'] + "']")))
        driver.find_element(By.XPATH, "//*[text()='" + arendator['Станция'] + "']").click()

        driver.find_element(*OrderScooterPageLocators.input_phone).send_keys(arendator['Телефон'])

        driver.find_element(*OrderScooterPageLocators.button_next).click()

    def complete_data_on_order_second_page(self, driver, arendator):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((OrderScooterPageLocators.arenda_text)))

        driver.find_element(*OrderScooterPageLocators.input_when).click()
        driver.find_element(By.XPATH, "//div[@aria-label='" + arendator['Когда привезти'] + "']").click()

        driver.find_element(*OrderScooterPageLocators.input_period).click()
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='" + arendator['Срок аренды'] + "']")))
        driver.find_element(By.XPATH, "//*[text()='" + arendator['Срок аренды'] + "']").click()

        driver.find_element(By.XPATH, "//label[text()='" + arendator['Цвет самоката'] + "']").click()

        driver.find_element(*OrderScooterPageLocators.input_comment).send_keys(arendator['Комментарий для курьера'])

        driver.find_elements(*OrderScooterPageLocators.order_button)[1].click()

    def cancel_order(self, driver):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((OrderScooterPageLocators.want_to_place_order_text)))

        driver.find_element(*OrderScooterPageLocators.cancel_button).click()

    def click_to_scooter_logo(self, driver):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((OrderScooterPageLocators.arenda_text)))
        driver.find_element(*OrderScooterPageLocators.link_scooter_logo).click()

        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((OrderScooterPageLocators.deliver_to_door_text)))

    def click_to_yandex_logo(selfself, driver):
        driver.find_element(*OrderScooterPageLocators.link_yandex_logo).click()

        driver.switch_to.window(driver.window_handles[-1])