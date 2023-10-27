import allure
import pytest

from selenium.webdriver.common.by import By
from questions_about_important_page import QuestionsAboutImportantPage

class TestQuestionsAboutImportant:
    @pytest.mark.parametrize(
        'accordeon_text,accordeon_panel_text',
        [
            ['Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
            ['Хочу сразу несколько самокатов! Так можно?',
             'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
            ['Как рассчитывается время аренды?',
             'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
            ['Можно ли заказать самокат прямо на сегодня?',
             'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
            ['Можно ли продлить заказ или вернуть самокат раньше?',
             'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
            ['Вы привозите зарядку вместе с самокатом?',
             'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
            ['Можно ли отменить заказ?',
             'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
            ['Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ]
    )
    @allure.title('Проверка отображения ответов на вопросы о важном')  # декораторы
    @allure.description('На главной странице находим аккордеон с вопросом, нажимаем на него и ожидаем увидеть ответ на вопрос')
    def test_questions_about_important(self, driver, accordeon_text, accordeon_panel_text):
        QuestionsAboutImportantPage.click_question_accordeon(self, driver, accordeon_text)

        QuestionsAboutImportantPage.check_answer_accordeon_is_visible(self, driver, accordeon_panel_text)

        element_for_check = driver.find_element(By.XPATH, "//p[text()='" + accordeon_panel_text + "']")
        expected_text = element_for_check.text

        assert expected_text == accordeon_panel_text