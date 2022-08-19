import pytest
from config.config import TestData
from Pages.SearchPage import SearchPage
from Tests.test_base import BaseTest


# запустить все тесты командoй: pytest Tests/test_SearchPage.py
# для запуска всех тестов и ведения журнала в формате html: pytest Tests/test_SearchPage.py -v --html=./hubSpot.html to
# запускать все тесты и логировать
#  в формат html при выполнении в параллельном режиме: pytest Tests/test_SearchPage.py -v -n 3 --html=./hubSpot.html


class TestSearchPage(BaseTest):

    # этот тест проверяет, поиск книги по автору
    def test_search_by_author(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.accept_cookies_policy()
        # найдите строку поиска и введите имя автора
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.AUTHOR_SEARCH)
        # найти имена авторов после завершения поиска
        self.search_result_list = self.searchPage.find_several_element(SearchPage.AUTHOR_NAME)
        # проверить, находится ли искомый автор в именах авторов книг, отображаемых в результате
        counter = 0
        for search_result in self.search_result_list:
            print(search_result.text)
            if self.searchPage.search_match_fully(search_result, TestData.AUTHOR_SEARCH):
                counter += 1
            else:
                counter = counter
        assert counter > 0

    # этот тест проверяет, есть  ли автор  в отображаемом описании книги
    def test_that_search_by_author_made_in_book_description(self):
        self.searchPage = SearchPage(self.driver)
        # найдите строку поиска и введите имя автора
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.AUTHOR_SEARCH)
        # найти описание книги после завершения поиска
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        # проверить, есть ли искомый автор в описании книг, отображаемых в результате
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.AUTHOR_SEARCH):
                counter += 1
            else:
                counter = counter
        assert counter > 0

    # этот тест проверяет, работает ли поиск по названию книги на кириллице
    def test_that_search_by_book_name_works(self):
        self.searchPage = SearchPage(self.driver)
        # найдите строку поиска и введите название книги
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.SEARCHED_BOOK_NAME)
        # найти описание книги после завершения поиска
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        # проверить, есть ли искомый автор в описании книг, отображаемых в результате
        counter = 0
        for search_result in self.search_result_list:

            if self.searchPage.search_match_fully(search_result, TestData.SEARCHED_BOOK_NAME):
                counter += 1
            else:
                pass
        assert counter > 0

    # этот тест проверяет, работает ли поиск по названию книги, если слова на кириллице набраны латиницей
    def test_that_search_by_book_name_works_if_russian_word_typed_by_latin(self):
        self.searchPage = SearchPage(self.driver)
        # найти строку поиска и отправить название книги (русское слово на латинице)
        self.searchPage.clear_text_and_send_text(SearchPage.SEARCH_FIELD, TestData.SEARCHED_RUSSIAN_BOOK_NAME_BY_LATIN)
        # найдите кнопку «Отправить поиск» и нажмите, чтобы начать поиск, и убедитесь, что кнопка работает
        self.searchPage.do_click(SearchPage.SEARCH_SUBMIT)
        # найти описание книги после завершения поиска
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        # проверить, есть ли искомый автор в описании книг, отображаемых в результате
        counter = 0
        for search_result in self.search_result_list:
            print(search_result.text)
            if self.searchPage.search_match_fully(search_result, TestData.EXPECTED_RESULT_BOOK_NAME):
                counter += 1
            else:
                pass
        assert counter > 0

    # этот тест проверяет, что кнопка "ВСЕ ФИЛЬТЫ" отображается в теле страницы открыть скрыть подменю "ВСЕ ФИЛЬТЫ"
    # и электронные книги будут удалены со страницы поиска после нажатия кнопки "Электронные книги"
    def test_that_submenu_search_opens_and_disabling_digital_books_works(self):
        self.searchPage = SearchPage(self.driver)
        # найти все книги, которые содержат ярлык "Электронные книги" под обложкой книги
        self.list_of_digital_books = self.searchPage.find_several_element(SearchPage.DIGITAL_BOOKS_LABEL)
        # найти элементы кнопки "ВСЕ ФИЛЬТРЫ" и нажать на кнопку
        button_to_open_all_filters = self.searchPage.find_several_element(SearchPage.ALL_FILTERS)
        # нажмите кнопку для отображения скрытого подменю "ВСЕ ФИЛЬТРЫ"
        button_to_open_all_filters[0].click()
        # отключить товары с пометкой "Электронные книги", нажав на кнопку "Электронные книги" в подменю, которое
        # появляется с левой стороны
        self.searchPage.do_click(SearchPage.DIGITAL_BOOKS_IN_ALL_FILTERS)
        # нажмите кнопку "Показать" в подменю для выполнения поиска
        self.searchPage.do_click(SearchPage.SHOW_RESULTS)
        # проверьте, чтобы на странице не было книг с пометкой "Электронные книги"
        for book in self.list_of_digital_books:
            assert self.searchPage.element_is_not_visible(book)

    # этот тест проверяет, что кнопка "Бумажные книги" отображается в теле страницы скрытие подменю "ВСЕ ФИЛЬТЫ" кликабельно
    # и после нажатия удалить из настроек поиска и быстрой кнопки "Бумажные книги" исчезнет из тела страницы
    def test_that_paper_book_button_in_hidden_submenu_remove_quick_button_from_page(self):
        self.searchPage = SearchPage(self.driver)
        # найти элементы кнопки "ВСЕ ФИЛЬТРЫ" и нажать на кнопку
        button_to_open_all_filters = self.searchPage.find_several_element(SearchPage.ALL_FILTERS)
        # нажмите кнопку для отображения скрытого подменю "ВСЕ ФИЛЬТРЫ"
        button_to_open_all_filters[0].click()
        # отключить товары с пометкой "Бумажные книги", нажав на кнопку "Бумажные книги" в появившемся подменю
        # с левой стороны
        self.searchPage.do_click(SearchPage.PAPER_BOOKS_IN_ALL_FILTERS)
        # нажмите кнопку "Показать" в подменю для выполнения поиска
        self.searchPage.do_click(SearchPage.SHOW_RESULTS)
        # убедитесь, что кнопка быстрого доступа "Бумажные книги" исчезла с тела страницы
        assert self.searchPage.is_not_visible(SearchPage.ENABLED_PAPER_BOOKS)

    # этот тест проверяет, что быстрая кнопка «В наличии», которая отображается в строке ниже кнопки «ВСЕ ФИЛЬТРЫ», кликабельна
    # и после клика удалить со страницы поиска все книги со статусом "В наличии" (имеются в виду все книги с кнопкой "В КОРЗИНУ"
    # исчезнут со страницы поиска)
    def test_that_quick_button_books_available_works(self):
        self.searchPage = SearchPage(self.driver)
        # найти все книги с помощью кнопки "В КОРЗИНУ" (книги в наличии)
        self.list_of_currently_available = self.searchPage.find_several_element(SearchPage.BUY_NOW_BUTTON)
        # найти быструю кнопку "В наличии", которая отображается в строке под кнопкой "ВСЕ ФИЛЬТРЫ"
        self.searchPage.do_click(SearchPage.BOOKS_AVAILABLE_CURRENTLY)
        # проверьте, чтобы все книги с кнопкой "В КОРЗИНУ" исчезли
        for book in self.list_of_currently_available:
            assert self.searchPage.element_is_not_visible(book)