from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage


class BasketPage(BasePage):

    """Локаторы"""

    BASKET_URL = "https://www.labirint.ru/cart/"

    #используется для теста с вводом количества в поле ввода
    QUANTITY_TO_ENTER = "7"

    # локатор логотипа "Лабиринт", по которому можно вернуться на главную


    # локатор кнопки "В КОРЗИНУ" под каждой книгой
    MOVE_BOOK_TO_BASKET = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), "В КОРЗИНУ")]')
    # локатор цен на книги
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]')
    # указатель окончательной стоимости книг,  на странице корзины
    PURCHASE_FINAL_SUM = (By.ID, "basket-default-sumprice-discount")
    # локатор кнопки "Очистить корзину" на странице корзины
    REMOVE_ALL_GOODS_IN_BASKET = (By.XPATH, '//a[@class="b-link-popup" and contains(text(), "Очистить корзину")]')
    # локатор для текста "Ваша корзина пуста. Почему?" который показывают, что корзина пуста
    BASKET_IS_EMPTY = (By.XPATH, '//span[contains(text(),"Ваша корзина пуста. Почему?")]')
    #локатор всплывающего окна с кнопкой "Оформить""
    POPUP_CHECKOUT_BOOK_BUTTON = (By.XPATH, '//a[@class="color_white btn btn-small btn-primary basket-go '
                                            'analytics-click-js"]')
    # локатор поля ввода для количества каждого предмета (книги) в пользовательском заказе на странице корзины,
    # которая отображается ниже каждого товара в корзине
    QUANTITY_OF_EACH_ITEM_IN_BASKET = (By.XPATH, '//input[@class="quantity"]')
    # локатор кнопки "+" увеличить количество товара (книги) в покупке на странице "Корзина"
    INCREASE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-increase btn-increase-cart"]')
    #локатор кнопки "-" уменьшить количество товара (книги) в покупке на странице корзины
    DECREASE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-lessen btn-lessen-cart"]')
    # локатор кнопки "Перейти к оформлению" , которая находится справа на странице корзины
    START_CHECKOUT = (By.XPATH, '//span[contains(text(), "Перейти к оформлению")]')
    #локатор кнопки "Оформить и оплатить" на странице оформления заказа
    CHECKOUT_AND_PAY = (By.XPATH, '//input[@value="Оформить и оплатить"]')

    """конструктор класса страницы"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Действия со страницей"""

    """узнать цену книги"""
    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)

    """этот метод удаляет все книги, если они есть в корзине, и возвращается на домашнюю страницу. """

    def remove_all_good_in_basket_and_reload_page(self):
        quantity = self.get_element_text(TestData.BASKET_COUNTER)
        if int(quantity) != 0:
            self.do_click(TestData.BASKET_BUTTON_AT_HEADER)
            self.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
            self.do_click(BasketPage.LABIRINT_MAIN_LOGO)