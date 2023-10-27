from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from questions_about_important_page_locators import QuestionsAboutImportantPageLocators

class QuestionsAboutImportantPage:

    def click_question_accordeon(self, driver, accordeon_text):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((QuestionsAboutImportantPageLocators.order_button)))

        element_for_click = driver.find_element(By.XPATH, "//*[text()='" + accordeon_text + "']")

        driver.execute_script("arguments[0].scrollIntoView();", element_for_click)
        element_for_click.click()

    def check_answer_accordeon_is_visible(self, driver, accordeon_panel_text):
        WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='" + accordeon_panel_text + "']")))