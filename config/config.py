from selenium.webdriver.common.by import By


class TestData:
    CHROME_EXECUTABLE_PATH = "C:/selenium_course/Skillfactory/Modul_28/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C:/selenium_course/Skillfactory/Modul_28/geckodriver.exe"

    BASE_URL = "https://www.labirint.ru/"

    # Данные ГЛАВНОЙ СТРАНИЦЫ для тестирования главного меню - тестирование кнопки "Книги"
    BOOKS_BUTTON_DESCRIPTION = "Книги"
    TITLE_OF_BOOK_PAGE = "Книги"
    TITLE_OF_MAIN_YEAR_BOOK_PAGE = "Главное 2022"
    ALL_BOOKS_TITLE = "Kниги"
    TEENS_BOOKS_TITLE = "Молодежная литература"
    PERIODICALS_TITLE = "Периодические издания"
    BILINGUAL_TITLE = "Билингвы"
    CHILD_BOOK_TITLE = "Детский досуг"
    MANGA_BOOK_TITLE = "Манга для детей"
    RELIGION_BOOK_TITLE = "Религии мира"

    # ТЕКУЩАЯ настройка региона
    CITY_TO_SET = "Новоросийск"
    CURRENT_CITY = "Новороссийск"

    # "москва" в кириллице
    CITY_TO_SET_IN_CYRILLIC = "Владивосток"
    FIRST_CITY_IN_AUTO_ADVICE = "Владивосток"

    CITY_TO_SET_WRONG_LANGUAGE = "Rfkbybyuhfl"
    FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC = "Калининград"

    # Данные для тестов PostponePage
    NUMBER_OF_BOOKS_TO_POSTPONE = 3

    # Сообщение об успешном удалении отложенных книг
    SUCCESSFUL_DELETION = "Выбранные товары удалены!"

    # Успешное удаление книг из корзины
    YOUR_BASKET_IS_EMPTY_TEXT = "ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?"

    # Имена атрибутов
    ATTRIBUTE_ID = "id"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_VALUE = "value"

    # Данные для страницы поиска
    AUTHOR_SEARCH = "Иван Тургенев"
    SEARCHED_BOOK_NAME = "Муму"
    SEARCHED_RUSSIAN_BOOK_NAME_BY_LATIN = "Uhfa Vjynt-Rhbcnj"  # "Граф Монте-Кристо"
    EXPECTED_RESULT_BOOK_NAME = "Граф Монте-Кристо"

    # Данные для фильтра страницы поиска
    MIN_PRICE = "500"
    MAX_PRICE = "600"

    """CROSS PAGE LOCATORS"""

    #локатор для кнопки, чтобы закрыть всплывающее окно, которое появляется после любого действия ("В Корзину", "ОТЛОЖИТЬ", etc)
    CLOSE_POPUP_ANY_ACTION = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    """for BASKET"""
    # локатор кнопки  "Корзина" в шапке
    BASKET_BUTTON_AT_HEADER = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main '
                                         'analytics-click-js cart-icon-js"]')

    # локатор счетчика кнопки "Корзина"
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

    """for Search"""