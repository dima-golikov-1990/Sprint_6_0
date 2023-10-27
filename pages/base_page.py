import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators

class BasePage:
    order_status_button = BasePageLocators.order_status_button
    order_button_in_top_page = BasePageLocators.order_button_in_top_page
    order_button_in_bottom_page = BasePageLocators.order_button_in_bottom_page

    link_scooter_logo = BasePageLocators.link_scooter_logo
    link_yandex_logo = BasePageLocators.link_yandex_logo

    def __init__(self, driver):
        self.driver = driver

    @allure.step('проверить что кнопка "Статус" отображается на странице')
    def check_button_order_is_visible(self):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((self.order_status_button)))

    @allure.step('взять элемент аккордеона по тексту')
    def get_accordeon_by_text(self, accordeon_text):
        return self.driver.find_element(By.XPATH, "//*[text()='" + accordeon_text + "']")

    @allure.step('кликнуть аккордеон')
    def click_accordeon(self, accordeon):
        self.driver.execute_script("arguments[0].scrollIntoView();", accordeon)
        accordeon.click()

    @allure.step('проверить отображение ответа после нажатия аккордеона')
    def check_accordeon_text_is_visible(self, accordeon_text):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='" + accordeon_text + "']")))

    @allure.step('проверить что кнопка "Заказать" отображается в верхней части страницы')
    def check_button_order_in_top_page_is_visible(self):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((self.order_button_in_top_page)))

    @allure.step('нажать кнопку "Заказать" в верхней части страницы')
    def click_button_order_in_top_page(self):
        self.driver.find_element(*self.order_button_in_top_page).click()

    @allure.step('нажать кнопку "Заказать" в нижней части страницы')
    def click_button_order_in_bottom_page(self):
        order_button = self.driver.find_element(*self.order_button_in_bottom_page)

        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        order_button.click()

    @allure.step('проверить что лого "Самокат" отображается на странице')
    def check_scooter_logo_is_visible(self):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((self.link_scooter_logo)))

    @allure.step('проверить что лого "Яндекс" отображается на странице')
    def check_yandex_logo_is_visible(self):
        WebDriverWait(self.driver, timeout=3).until(EC.visibility_of_element_located((self.link_yandex_logo)))

    @allure.step('нажать на лого "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*self.link_scooter_logo).click()

    @allure.step('нажать на лого "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*self.link_yandex_logo).click()

    @allure.step('переключиться на вторую вкладку в браузере')
    def switch_to_second_tab_in_browser(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('переключиться на вторую вкладку в браузере')
    def get_accordeon_answer_text(self,accordeon_text):
        return self.driver.find_element(By.XPATH, "//p[text()='" + accordeon_text + "']").text