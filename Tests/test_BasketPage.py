import time

from Pages.BasketPage import BasketPage
from Tests.test_base import BaseTest
from config.config import TestData
from Pages import  BasePage

# запустить все тесты командoй: pytest Tests/test_BasketPage.py
# для запуска всех тестов и ведения журнала в формате html: pytest Tests/test_BasketPage.py -v --html=./hubSpot.html
# запускать все тесты и логировать
# в формат html при выполнении в параллельном режиме: pytest Tests/test_BasketPage.py -v -n 3 --html=./hubSpot.html


class TestBasketFmHomePage(BaseTest):

    # этот тест находит первую книгу на главной странице и получает цену книги, затем перемещает эту книгу в корзину и проверяет цену
    # эта книга в корзине не меняется
    def test_first_book_moved_in_basket_and_price_is_same(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.accept_cookies_policy()
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти добавить  "В КОРЗИНУ" первой книги на главной странице
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # найти все цены на все книги
        self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на главной странице
        first_book_price_element = self.list_of_book_prices[0]
        # получить (int) цену первой книги
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # нажмите на кнопку "В КОРЗИНУ" первой книги
        fist_book_button_move_into_basket.click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все цены на все книги в корзине на странице корзины
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на странице корзины
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # получить (int) цену первой книги в корзине
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        assert first_book_price == first_book_price_in_basket

    # тест проверяет, что кнопка "Очистить корзину" отображается справа над деталями заказа, очищает корзину
    def test_that_clear_basket_button_clean_basket(self):
        self.basketPage = BasketPage(self.driver)
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти и добавить в корзину "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все цены на все книги в корзине на странице корзины
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на странице корзины
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        self.basketPage.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
        result = self.basketPage.get_element_text(BasketPage.BASKET_IS_EMPTY)
        assert self.basketPage.element_is_not_visible(price_of_first_book_string)
        assert result.lower() == TestData.YOUR_BASKET_IS_EMPTY_TEXT.lower()

    # этот тест находит первую книгу на главной странице и получает цену книги, затем перемещает эту книгу в корзину и проверяет цену
    # данная книга в Корзине не меняется и равна итоговой сумме заказа "Подитог без учета доставки"
    def test_first_book_moved_in_basket_and_price_is_same_and_equal_final_sum(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти кнопку добавить  "В КОРЗИНУ" первой книги на главной странице
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # найти все цены на все книги
        self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на главной странице
        first_book_price_element = self.list_of_book_prices[0]
        # получить (int) цену первой книги
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # нажмите на кнопку "В КОРЗИНУ" первой книги
        fist_book_button_move_into_basket.click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все цены на все книги в корзине на странице корзины
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на странице корзины
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # получить (int) цену первой книги в корзине
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # получить окончательную сумму купленных книг
        final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
        assert (first_book_price and first_book_price_in_basket) == int(final_sum)

    # этот тест находит первую книгу на главной странице и получает цену книги, затем перемещает эту книгу в корзину и проверяет цену
    # данная книга в Корзине не меняется и равна итоговой сумме заказа "Подытог без учета доставки"
    def test_that_button_in_popup_window_leads_to_basket(self):
        self.basketPage = BasketPage(self.driver)
        # find all buttons "В КОРЗИНУ" at Home page
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти добавить в корзину "В КОРЗИНУ" первую книгу на главной странице
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # нажмите на кнопку "В КОРЗИНУ" первой книги
        fist_book_button_move_into_basket.click()
        # нажмите кнопку "Оформить" во всплывающем окне действия
        self.basketPage.find_several_element(BasketPage.POPUP_CHECKOUT_BOOK_BUTTON)[0].click()
        assert self.basketPage.get_current_url() == BasketPage.BASKET_URL

    # этот тест проверяет, что начальное количество товара (книги), добавленного в корзину кнопкой "В КОРЗИНУ", равно "1" (одна штука)
    def test_that_initial_quantity_of_item_added_in_basket_is_one(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти и добавить в корзину "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все поля ввода количества всех предметов
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # найти поле ввода последнего добавленного элемента
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # найти количество последнего добавленного товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) == 1

    # этот тест проверяет, что количество товара (книги), добавленного в корзину кнопкой "В КОРЗИНУ", увеличилось
    # по нажатию кнопки  "+"
    def test_that_quantity_of_item_added_in_basket_can_be_increased(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти и добавить  "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все поля ввода количества всех предметов
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # найти поле ввода последнего добавленного элемента
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # найти количество последнего добавленного товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # найти все кнопки "+"
        self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.INCREASE_QUANTITY_OF_ITEM)
        # увеличить количество последнего добавленного предмета на одну штуку нажатием  на кнопку "+"
        self.basketPage.driver.execute_script("arguments[0].scrollIntoView();", self.list_of_increase_buttons[0])
        self.list_of_increase_buttons[0].click()
        # запросить повторно количество последнего добавленного товара
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(new_quantity_of_first_book) - int(quantity_of_first_book) == 1

    # этот тест проверяет, что количество товара (книги), добавленного в корзину кнопкой "В КОРЗИНУ", должно быть изменено
    # ввод цифр в поле ввода, расположенное под элементом слева от кнопки "-"
    def test_that_quantity_can_set_by_enter_digits_into_input_field(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти и добавить в корзину "В КОРЗИНУ" первую книгу на главной странице
        self.basketPage.driver.execute_script("arguments[0].scrollIntoView();", self.list_of_buttons_move_into_basket[0])
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все поля ввода количества всех предметов
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # найти поле ввода последнего добавленного элемента
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # найти количество последнего добавленного товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # отправить количество в поле ввода
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # сделать новый запрос количества
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) == 1
        assert int(new_quantity_of_first_book) == int(BasketPage.QUANTITY_TO_ENTER)

    # этот тест проверяет, что количество товара (книги), добавленного в корзину кнопкой "В КОРЗИНУ", уменьшилось на
    # нажатие кнопки "-"
    def test_that_quantity_can_decreased_by_pressing_decrease_button(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти и добавить в корзину "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все поля ввода количества всех предметов
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # найти поле ввода для  количества последнего добавленного элемента
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # отправить количество в поле ввода
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)

        time.sleep(5)
        # найти количество последнего добавленного товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        print(quantity_of_first_book)
        # найти все кнопки "-"
        self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.DECREASE_QUANTITY_OF_ITEM)
        self.basketPage.driver.execute_script("arguments[0].scrollIntoView();", self.list_of_increase_buttons[0])
        # уменьшить количество последнего добавленного предмета на одну штуку нажатием единицы на кнопку "-"
        self.list_of_increase_buttons[0].click()
        time.sleep(5)
        # запросить повторно количество последнего добавленного товара
        #new_quantity_of_first_book = first_book_input_field.get_attribute("value")
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        print(new_quantity_of_first_book)
        assert int(quantity_of_first_book) - int(new_quantity_of_first_book) == 1

    # проверить, что цена товара (книги), добавленного в корзину кнопкой "В КОРЗИНУ", меняется в соответствии с новым количеством
    def test_that_sum_will_raise_accordingly_when_quantity_of_item_increased(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все поля ввода количества всех предметов
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # найти все цены на все книги в корзине на странице корзины
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на странице корзины
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # получить (int) цену первой книги в корзине
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # найти поле ввода последнего добавленного элемента
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # отправить количество для первой книги в поле ввода
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # из-за изменения количества и суммы требуется около 3-5 секунд, необходимо обновить страницу или установить time.sleep
        time.sleep(5)
        # найти все цены на все книги в корзине на странице корзины
        self.list_of_book_prices_in_basket_new = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на странице корзины
        price_of_first_item = self.list_of_book_prices_in_basket_new[0]
        # получить (int) цену первого товара в корзине с новым количеством
        new_price = self.basketPage.price_by_int(price_of_first_item)
        assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER)) == new_price

    # проверьте окончательную цену "Подытог без учета доставки" всех товаров (книг), добавленных  "В КОРЗИНУ"
    # кнопка меняется в зависимости от нового количества
    def test_that_final_sum_will_raise_accordingly_when_quantity_of_item_increased(self):
        self.basketPage = BasketPage(self.driver)
        # закрываем всплывающее окно с предложением принять куки
        self.basketPage.accept_cookies_policy()
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # добавить две книги в корзину
        for book in self.list_of_buttons_move_into_basket[0:2]:
            book.click()
        # закрыть всплывающее окно действия
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # найти все поля ввода количества всех предметов
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # найти все цены на все книги в корзине на странице корзины
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # найти элемент, который содержит цену первой книги на странице корзины
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # найти элемент, который содержит цену первой книги на странице корзины
        price_of_second_book_string = self.list_of_book_prices_in_basket[1]
        # получить (int) цену первой книги в корзине
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # получить (int) цену второй книги в корзине
        second_book_price_in_basket = self.basketPage.price_by_int(price_of_second_book_string)
        # найти поле ввода последнего добавленного элемента
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # отправить количество для первой книги в поле ввода
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # из-за изменения количества и суммы требуется около 3-5 секунд, необходимо обновить страницу или установить time.sleep
        time.sleep(5)
        # получить окончательную сумму купленных книг
        final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
        assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER) + second_book_price_in_basket) == int(final_sum)

    # этот тест проверяет, что кнопка «Оформить», отображаемая, ведет на страницу оформления заказа.
    def test_that_start_checkout_button_open_checkout_page(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # закрываем всплывающее окно с предложением принять куки
        self.basketPage.accept_cookies_policy()
        # найти все кнопки "В КОРЗИНУ" на Главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # найти и добавить в корзину "В КОРЗИНУ" первую книгу на главной странице
        self.list_of_buttons_move_into_basket[0].click()
        # close popup action window
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажмите на кнопку "Корзина" в шапке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # нажмите кнопку "Начать оформление"
        self.basketPage.do_click(BasketPage.START_CHECKOUT)

        assert 'https://www.labirint.ru/cart/checkout/' == BasketPage.BASKET_URL + "checkout/"

