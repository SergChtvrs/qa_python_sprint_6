import pytest
import allure
from pages.main_page import MainPage
from data import AnswerText


class TestMainPage:
    @allure.title('Проверка текста ответов в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('num, answer_text', [
        (0, AnswerText.ANSWER_TEXT_1),
        (1, AnswerText.ANSWER_TEXT_2),
        (2, AnswerText.ANSWER_TEXT_3),
        (3, AnswerText.ANSWER_TEXT_4),
        (4, AnswerText.ANSWER_TEXT_5),
        (5, AnswerText.ANSWER_TEXT_6),
        (6, AnswerText.ANSWER_TEXT_7),
        (7, AnswerText.ANSWER_TEXT_8)
        ],
        ids=['вопрос 0',
             'вопрос 1',
             'вопрос 2',
             'вопрос 3',
             'вопрос 4',
             'вопрос 5',
             'вопрос 6',
             'вопрос 7'])
    def test_accordion_answers_text(self, driver, num, answer_text):
        main_page = MainPage(driver)
        main_page.cookies_acceptation()
        assert main_page.get_answer_text(num) == answer_text
