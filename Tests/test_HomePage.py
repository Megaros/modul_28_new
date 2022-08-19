from config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


# запустить все тесты командой: pytest Tests/test_HomePage.py
# для запуска всех тестов и ведения журнала в формате html: pytest Tests/test_HomePage.py -v --html=./hubSpot.html
# для запуска всех тестов и ведения журнала в формате html в параллельном режиме выполнения: pytest Tests/test_HomePage.py -v -n 3 --html=./hubSpot.html


class TestHomePageMainMenu(BaseTest):

    # проверить, что кнопка "Книги" видна
    def test_books_button_visible(self):
        self.homePage = HomePage(self.driver)
        button = self.homePage.is_visible(HomePage.BOOKS)
        assert button == True

    # проверить, что кнопка "Книги" имеет правильное имя
    def test_books_button_has_proper_name(self):
        self.homePage = HomePage(self.driver)
        button_name = self.homePage.get_element_text(HomePage.BOOKS)
        assert button_name == TestData.BOOKS_BUTTON_DESCRIPTION

    # тестовая кнопка "Книги" кликабельна и ведет на нужную страницу
    def test_books_button_clickable(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.BOOKS)
        book_page_header = self.homePage.get_element_text(HomePage.BOOKS_PAGE_HEADER)
        assert book_page_header == TestData.TITLE_OF_BOOK_PAGE

    # тестовое подменю "Главное 2022" кнопки "Книги" кликабельно и ведет на нужную страницу - подменю "Главное 2022"
    def test_submenu_books_of_year_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.MAIN_OF_THE_YEAR)
        books_main_of_the_year_title = self.homePage.get_element_text(HomePage.MAIN_OF_THE_YEAR_HEADER)
        assert books_main_of_the_year_title == TestData.TITLE_OF_MAIN_YEAR_BOOK_PAGE

    # тестовое подменю "Все книги" кнопки "Книги" кликабельно и ведет на нужную страницу - подменю "Книги"
    def test_submenu_all_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.ALL_BOOKS)
        all_books_title = self.homePage.get_element_text(HomePage.BOOKS_PAGE_HEADER)
        assert all_books_title == TestData.TITLE_OF_BOOK_PAGE

    # тестовое подменю "Молодежная литература" кнопки "Книги" кликабельно и ведет на нужную страницу - подменю "Книги"
    def test_submenu_teens_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.TEENS_BOOKS)
        teens_books_title = self.homePage.get_element_text(HomePage.TEENS_BOOKS_HEADER)
        assert teens_books_title == TestData.TEENS_BOOKS_TITLE

    # тестовое подменю "Периодические издания" кнопки "Книги" кликабельно и ведет на нужную страницу - подменю "Книги"
    def test_periodicals_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.PERIODICAL_BOOKS)
        periodicals_title = self.homePage.get_element_text(HomePage.PERIODICAL_BOOKS_HEADER)
        assert periodicals_title == TestData.PERIODICALS_TITLE

    # test submenu "Билингвы и книги на иностранных языках" of button "Книги" is clickable and leads to proper page - submenu "Билингвы"
    def test_bilingual_in_book_button_at_second_submenu(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_second_level(HomePage.BOOKS, HomePage.BILINGUAL_FIRST_SUBMENU,
                                                                HomePage.BILINGUAL_BOOKS)
        bilingual_title = self.homePage.get_element_text(HomePage.BILINGUAL_BOOKS_HEADER)
        assert bilingual_title == TestData.BILINGUAL_TITLE

    # тестовое подменю "Комиксы, Манга, Артбуки" кнопки "Книги" кликабельно и ведет на нужную страницу - подменю "Манга"
    def test_manga_in_book_button_at_second_submenu(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_second_level(HomePage.BOOKS, HomePage.MANGA_FIRST_SUBMENU,
                                                                HomePage.MANGA_BOOKS)
        manga_books_title = self.homePage.get_element_text(HomePage.MANGA_BOOKS_HEADER)
        assert manga_books_title == TestData.MANGA_BOOK_TITLE

    # тестовое подменю "Религии" кнопки "Книги" кликабельно и ведет на страницу - подменю  "Религии мира"
    def test_religion_in_book_button_at_second_submenu(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_second_level(HomePage.BOOKS, HomePage.RELIGION_FIRST_SUBMENU,
                                                                HomePage.RELIGION_BOOKS)
        religion_books_title = self.homePage.get_element_text(HomePage.RELIGION_BOOKS_HEADER)
        assert religion_books_title == TestData.RELIGION_BOOK_TITLE

    # тест для установки текущего региона
    def test_to_set_current_region(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.REGION_CURRENT_SETTING)
        self.homePage.clear_text_and_send_text_with_enter(HomePage.REGION_SEARCH_FIELD, TestData.CITY_TO_SET)
        city_after_setting = self.homePage.get_element_text(HomePage.REGION_CURRENT_SETTING)
        assert city_after_setting == TestData.CURRENT_CITY

    # проверить автоподсказку для установки текущего региона в кириллице, дать правильный вариант кириллицы
    def test_auto_advice_to_set_current_region_in_cyrillic_works(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.REGION_CURRENT_SETTING)
        self.homePage.clear_text_and_send_text(HomePage.REGION_SEARCH_FIELD, TestData.CITY_TO_SET_IN_CYRILLIC)
        self.auto_advice_cities = self.homePage.find_several_element(HomePage.REGION_GUESS_LUST)
        first_city_in_list = self.auto_advice_cities[0]
        assert TestData.FIRST_CITY_IN_AUTO_ADVICE in first_city_in_list.text

    # протестировать автоподсказку для установки текущего региона при вводе кириллического имени на английском языке
    # дать правильный кириллический вариант
    def test_auto_advice_to_set_current_region_in_wrong_language_works(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.REGION_CURRENT_SETTING)
        self.homePage.clear_text_and_send_text(HomePage.REGION_SEARCH_FIELD, TestData.CITY_TO_SET_WRONG_LANGUAGE)
        self.auto_advice_cities = self.homePage.find_several_element(HomePage.REGION_GUESS_LUST)
        first_city_in_list = self.auto_advice_cities[0]
        assert TestData.FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC in first_city_in_list.text

    # тест установки текущего Региона в кириллице в автосовете с правильным кириллическим названием
    def test_to_set_current_region_in_cyrillic_works_via_auto_advice(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.REGION_CURRENT_SETTING)
        self.homePage.clear_text_and_send_text(HomePage.REGION_SEARCH_FIELD, TestData.CITY_TO_SET_IN_CYRILLIC)
        self.auto_advice_cities = self.homePage.find_several_element(HomePage.REGION_GUESS_LUST)
        self.auto_advice_cities[0].click()
        assert self.homePage.get_element_text(HomePage.REGION_CURRENT_SETTING) == TestData.FIRST_CITY_IN_AUTO_ADVICE

    # тестовая установка текущего Региона в кириллице в автосовете с кириллическим именем отправить латиницей
    def test_to_set_current_region_entered_cyrillic_by_latin_letters_works_via_auto_advice(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.REGION_CURRENT_SETTING)
        self.homePage.clear_text_and_send_text(HomePage.REGION_SEARCH_FIELD, TestData.CITY_TO_SET_WRONG_LANGUAGE)
        self.auto_advice_cities = self.homePage.find_several_element(HomePage.REGION_GUESS_LUST)
        self.auto_advice_cities[0].click()
        assert self.homePage.get_element_text(HomePage.REGION_CURRENT_SETTING) == TestData.FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC

    # проверить, что всплывающее окно появляется при наведении на кнопку "Сообщение" (имейте в виду, что "is_visible"
    # - это логический метод)
    def test_popup_window_message_button_appear(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MESSAGE_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MESSAGE_BUTTON_WINDOW)
        assert popup_window is True

    # проверить, чтобы всплывающее окно появлялось при наведении на кнопку "Сообщение" и исчезало при перемещении курсора
    def test_popup_window_message_button_disappeared(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MESSAGE_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MESSAGE_BUTTON_WINDOW)
        assert popup_window is True
        self.homePage.move_away_from_element(HomePage.LABIRINT_MAIN_LOGO)
        window_disappeared = self.homePage.is_not_visible(HomePage.POPUP_MESSAGE_BUTTON_WINDOW)
        assert window_disappeared is True

    # проверить, что всплывающее окно появляется при наведении на кнопку "Мой Лабиринт"
    # ( "is_visible" - это логический метод)
    def test_popup_window_my_labyrinth_button_appear(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MY_LABIRINT_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MY_LABIRINT_BUTTON_WINDOW)
        assert popup_window is True

    # проверить, чтобы всплывающее окно появлялось при наведении на кнопку "Мой Лабиринт"
    # и исчезало при отведении курсора
    def test_popup_window_my_labyrinth_button_disappeared(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.MY_LABIRINT_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_MY_LABIRINT_BUTTON_WINDOW)
        assert popup_window is True
        self.homePage.move_away_from_element(HomePage.LABIRINT_MAIN_LOGO)
        window_disappeared = self.homePage.is_not_visible(HomePage.POPUP_MY_LABIRINT_BUTTON_WINDOW)
        assert window_disappeared is True

    # проверить, что всплывающее окно появляется при наведении на кнопку "Отложено"
    # ( "is_visible" - это логический метод)
    def test_popup_window_postponed_button_appear(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.POSTPONED_BOOKS_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_POSTPONED_BOOKS_WINDOW)
        assert popup_window is True

    # проверить, чтобы всплывающее окно появлялось при наведении на кнопку "Отложено"
    # и исчезало при перемещении курсора
    def test_popup_window_my_postponed_button_disappeared(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_show_submenu(HomePage.POSTPONED_BOOKS_BUTTON)
        popup_window = self.homePage.is_visible(HomePage.POPUP_POSTPONED_BOOKS_WINDOW)
        assert popup_window is True
        self.homePage.move_away_from_element(HomePage.LABIRINT_MAIN_LOGO)
        window_disappeared = self.homePage.is_not_visible(HomePage.POPUP_POSTPONED_BOOKS_WINDOW)
        assert window_disappeared is True