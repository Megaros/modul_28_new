from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """Локаторы"""
    URL = TestData.BASE_URL

    # локатор логотипа "Лабиринт", по которому можно вернуться на главную
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # локатор для кнопки "Принять" принять политику использования файлов cookie
    COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    # локаторы строки главного меню для кнопки "Книги" и кнопок подменю
    BOOKS = (By.XPATH, '//a[@class="b-header-b-menu-e-text" and contains(text(), "Книги")]')
    BOOKS_PAGE_HEADER = (By.XPATH, '//h1[@class="genre-name"]')
    MAIN_OF_THE_YEAR = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Главное 2022")] ')
    MAIN_OF_THE_YEAR_HEADER = (By.XPATH, '//a[@class="b-header-b-menu-e-text" and contains(text(), "Главное 2022")]')
    ALL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Все книги")]')
    #  ALL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Книги")]')
    TEENS_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Молодежная '
                             'литература")]')
    TEENS_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Молодежная литература")]')
    PERIODICAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                                  '"Периодические издания")]')
    PERIODICAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Периодические издания")]')

    # локаторы строки главного меню для кнопки "Книги" для типа книг во втором скрытом подменю
    BILINGUAL_FIRST_SUBMENU = (By.XPATH,
                               '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), '
                               '"Билингвы и книги на иностранных языках")]')
    BILINGUAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Билингвы")]')
    BILINGUAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Билингвы")]')

    CHILD_BOOKS_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains('
                                           'text(), "Книги для детей")]')
    CHILD_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Детский досуг")]')
    #CHILD_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Детский досуг")]')

    MANGA_FIRST_SUBMENU = (By.XPATH,
                           '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Комиксы, '
                           'Манга, Артбуки")]')
    MANGA_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Манга для детей")]')
    MANGA_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Манга для детей")]')

    RELIGION_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Религия")]')
    RELIGION_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Религии мира")]')
    RELIGION_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Религии мира")]')

    #локаторы для настройки местоположения региона пользователя
    REGION_ICON_BUTTON = (By.XPATH, '//span[@class="region-location-icon region-location-icon-m-hover-hide b-header-e-sprite-background"]')
    REGION_CURRENT_SETTING = (By.XPATH, '//span[@class="region-location-icon-txt "]')
    REGION_SEARCH_FIELD = (By.ID, "region-post")
    # локатор для автоподсказки в поле региона поиска
    REGION_GUESS_LUST = (By.XPATH, '//a[@class="a-item"]')

    # локаторы для панели заголовка
    #для кнопки "Сообщения"
    MESSAGE_BUTTON = (By.XPATH, '//span[@class="b-header-b-personal-e-text" and contains(text(), "Сообщения")]')
    # для всплывающего окна "Сообщения"
    POPUP_MESSAGE_BUTTON_WINDOW = (By.XPATH, '//div[@class="b-menu-list-title font_regular"]')

    # для кнопки "Мой Лабиринт"
    MY_LABIRINT_BUTTON = (By.XPATH, '//li[@class="b-header-b-personal-e-list-item have-dropdown b-header-b-personal-e-list-item_cabinet"]')
    POPUP_MY_LABIRINT_BUTTON_WINDOW = (By.XPATH, '//a[contains(text(), "Вход или регистрация в Лабиринте")]')

    # для кнопки "Отложено"
    POSTPONED_BOOKS_BUTTON = (By.XPATH,
                              '//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-putorder b-header-e-sprite-background"]')
    POPUP_POSTPONED_BOOKS_WINDOW = (By.XPATH, '//div[contains(text(), "Здесь будут храниться ваши отложенные товары.")]')

    """конструктор класса страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Действия со страницей"""

    """функция используется для получения заголовка страницы"""

    def get_home_page_title(self, title):
        return self.get_title(title)

    """функция используется для перемещения курсора от элемента к желаемому элементу"""

    def move_away_from_element(self, by_locator):
        element_to_move = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(element_to_move).perform()