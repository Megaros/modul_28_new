from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage


class SearchPage(BasePage):
    """Локаторы"""
    URL = TestData.BASE_URL + "search/"

    # локатор логотипа "Лабиринт", по которому можно вернуться на главную
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # локатор для кнопки "Принять" принять политику использования файлов cookie
    COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    # локатор для поля ввода Поиск в шапке "Поиск по Лабиринту"
    SEARCH_FIELD = (By.XPATH, "//input[@id='search-field']")
    # локатор для кнопки отправки поиска
    SEARCH_SUBMIT = (By.XPATH, '//button[@class="b-header-b-search-e-btn"]')

    # локатор имени автора
    AUTHOR_NAME = (By.XPATH, '//div[@class="product-author"]')
    # локатор для описания книги, которое находится под обложкой книги
    BOOK_DESCRIPTION = (By.XPATH, '//a[@class="product-title-link"]')

    # локаторы для Подменю "ВСЕ ФИЛЬТРЫ"
    # кнопка "ВСЕ ФИЛЬТРЫ", которая находится в теле страницы и открывает скрытое подменю слева
    ALL_FILTERS = (By.XPATH, '//span[@class="navisort-item__content" and contains(text(), "ВСЕ ФИЛЬТРЫ")]')
    # кнопка "Бумажные книги" в подменю "ВСЕ ФИЛЬТРЫ" для включения/выключения книг из поиска
    PAPER_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Бумажные книги")]')
    # кнопка "Электронные книги" в подменю "ВСЕ ФИЛЬТРЫ" для включения/выключения книг из поиска
    DIGITAL_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Электронные книги")]')
    # кнопка "Показать" в конце подменю "ВСЕ ФИЛЬТРЫ" для проверки настроек фильтра
    SHOW_RESULTS = (By.XPATH, '//input[@class="show-goods__button" and @value="Показать"]')
    # кнопка "ЦЕНА", при нажатии на которую появляется скрытое подменю для настройки цены
    PRICE_MENU_BUTTON = (By.XPATH, '//div[@class="bl-name" and contains(text(), "ЦЕНА")]')
    # поле ввода, чтобы установить минимальную цену товаров для поиска
    SET_MIN_PRICE = (By.XPATH, '//input[@name="price_min"]')
    # поле ввода, чтобы установить максимальную цену товаров для поиска
    SET_MAX_PRICE = (By.XPATH, '//input[@name="price_max"]')

    # локатор для кнопки быстрого доступа, которая показывает текущую настройку поиска, отображаемую в теле страницы под кнопкой "ВСЕ ФИЛЬТРЫ"
    # локатор, показывающий, что "Бумажные книги" включены (эта кнопка удаляет этот параметр из поиска при нажатии)
    ENABLED_PAPER_BOOKS = (By.XPATH, '//div[contains(text(), "Бумажные книги")]')
    # локатор, показывающий, что "В наличии" включен (эта кнопка удаляет этот параметр из поиска при нажатии)
    BOOKS_AVAILABLE_CURRENTLY = (By.XPATH, '//div[@class="filter-reset__content" and contains(text(), "В наличии")]')
    ALL_CURRENT_SETTINGS = (By.XPATH, '//div[@class="filter-reset__content"]')

    # локаторы для элементов, отображаемых под обложкой книги
    # указатель этикетки "ЭЛЕКТРОННАЯ КНИГА", которая находится под обложкой книги
    DIGITAL_BOOKS_LABEL = (By.XPATH, '//span[@class="card-label__text card-label__text_inversed" and contains(text(),"Электронная книга")]')
    # локатор для кнопки "КУПИТЬ" отображается только если книга в наличии в данный момент в магазине
    BUY_NOW_BUTTON = (By.XPATH, '//a[@class="btn buy-link js-ebooks-buy-btn btn-primary" and contains(text(), "КУПИТЬ")]')

    # локатор цен на книги
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]/span')
    # локатор для кнопки страницы пагинации (для пробного использования страницы 2)
    PAGINATION_PAGE_BUTTON = (By.XPATH, '//a[@class="pagination-next__text" and contains(text(), "Следующая")]')

    """конструктор класса страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchPage.URL)

    """Действия со страницей"""

    """чтобы проверить, все ли "слова поиска" находятся в текстовом результате, если результат был найден в значении атрибута"""

    def search_match_fully(self, element, search_name):
        element_text = element.get_attribute(TestData.ATTRIBUTE_TITLE)
        element_in_list = element_text.lower().split()
        name_list = search_name.lower().split()
        result = list(set(element_in_list) & set(name_list))
        return len(name_list) == len(result)

    """узнать цену книги"""

    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)