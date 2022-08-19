from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage


class PostponePage(BasePage):
    """Локаторы"""

    URL = TestData.BASE_URL

    # локатор логотипа "Лабиринт", по которому можно вернуться на главную
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # Для кнопки  "Отложено"
    POSTPONED_BOOKS_BUTTON = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    #для символа "сердце" - "отложить" для книг на Главной странице в разделе "Что почитать: выбор редакции"
    #HEART_SYMBOL_AT_HOME_PAGE = (By.XPATH, '//a[@data-tooltip_title="Отложить"]')
    # локатор для всплывающего окна, которое появляется после нажатия на символ «сердце»
    POPUP_BOOK_POSTPONED = (By.XPATH, '//div[contains(text(), "Вы добавили  в отложенные книгу ")]')
    # локатор для кнопки, которая закрывает всплывающее окно, предупреждающее, что книга отложена
    CLOSE_POPUP_BOOK_POSTPONED = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')
    # локатор количества отложенных книг в шапке страницы
    QUANTITY_OF_POSTPONED_BOOKS = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-putorder basket-in-dreambox-a"]')
    # локатор для удаления книги из отложенной
    DELETE_POSTPONED_BOOK = (By.XPATH, '//span[@class="b-list-item-hover pointer"]')
    # для описания книг в разделе "Отложено"
    BOOKS_DESCRIPTION_COVER = (By.XPATH, '//a[@class="cover"]')
    # кнопка локатора "Все отложенные товары" во всплывающем окне, которое появляется после наведения на иконку "Отложено"
    BUTTON_IN_POSTPONE_ICON_POPUP = (By.XPATH, '//a[@class="btn btn-middle btn-clear font_size_s all-putorder-btn-js"]')

    # для названия книги на "labirint.ru/cabinet/putorder/"=страница отложенной книги
    BOOK_IN_POSTPONE_PAGE = (By.XPATH, '//span[@class="product-title"]')

    # локатор кнопки "Очистить" на странице "Отложить" "https://www.labirint.ru/cabinet/putorder/"
    CLEAR_POSTPONE_BUTTON = (By.XPATH, '//a[@title="Удалить все отложенные товары"]')
    # locator for Postpone page message "Сообщение Выбранные товары удалены!"
    POSTPONED_BOOKS_DELETED_MESSAGE = (By.XPATH, '//p[contains(text(),"Выбранные товары удалены!")]')

    # локатор кнопки "Выделить все" на странице "Отложено"
    SELECT_ALL_POSTPONED_BOOKS = (By.XPATH, '//a[@title="Выделить все отложенные товары"]')
    # локаторы флажков для отметки книг на отложенной странице
    CHECKBOX_POSTPONED_BOOKS = (By.XPATH, '//label[@class="checkbox-ui checkbox-ui-m-bg checkbox-ui-m-multi checkbox-ui-m-big"]')
    # локатор кнопки «Удалить» во всплывающем меню, которое появляется, если какой-либо из флажков для пометки книги был включен
    DELETE_SELECTED_BOOKS = (By.XPATH, '//a[contains(text(),"Удалить")]')
    # локатор для краткого описания всех отложенных книг на странице «Отложено»
    ALL_SELECTED_BOOKS = (By.XPATH, '//div[@class="product-cover short-title"]')
    # локатор кнопки "В КОРЗИНУ", которая находится под отложенной книгой на странице "Отложить"
    MOVE_IN_BASKET_FM_POSTPONE_BUTTON = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), "В КОРЗИНУ")]')
    # локатор кнопки "ОФОРМИТЬ", которая размещается под отложенной книгой на странице "Отложить", если книга была добавлена в
    # корзину кнопкой "В КОРЗИНУ"
    SWITCH_TO_CHECKOUT_BOOK_IN_BASKET_FM_POSTPONE_PAGE = (By.XPATH, '//a[@class="btn buy-link btn-primary btn-more" and contains(text(), "ОФОРМИТЬ")]')
    # локатор для кнопки, которая закрывает всплывающее окно, предупреждающее, что книга отложена
    CLOSE_POPUP_POSTPONED_BOOK_MOVED_IN_BASKET = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')
    # локатор для кнопки "Перенести в отложенные"
    HEART_SYMBOL_AT_HOME_PAGE = (By.XPATH, '//a[@data-tooltip_title="Отложить"]')

    """конструктор класса страницы"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Действия со страницей"""

    """функция используется для получения заголовка страницы"""
    def get_home_page_title(self, title):
        return self.get_title(title)

    """этот метод очищает отложенные книги на странице «Отложенная книга» и возвращается на домашнюю страницу. Метод был создан из-за
    подозрение, что  файлы cookie не полностью удаляются при перезагрузке страницы после запуска нового теста"""
    def clear_postpone_reload_page(self):
        self.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        if self.is_visible(PostponePage.CLEAR_POSTPONE_BUTTON):
            self.do_click(PostponePage.CLEAR_POSTPONE_BUTTON)
            alert = self.driver.switch_to.alert
            alert.accept()
        self.do_click(PostponePage.LABIRINT_MAIN_LOGO)