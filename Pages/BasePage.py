from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Этот класс является родителем всех страниц
   он содержит все общие методы и утилиты для всех страниц"""

# локатор для кнопки "Принять" принять политику использования файлов cookie
COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """ожидание элемента и нажатие на элемент"""
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    """отправить ключи в поле ввода"""
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """чтобы очистить поле поиска, отправить другой ключ в поле поиска"""
    def clear_text_and_send_text(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(2)
        input_field.clear()
        input_field.send_keys(text)

    """чтобы очистить поле поиска, отправьте другой ключ в поле поиска и нажатие  клавишы ENTER"""
    def clear_text_and_send_text_with_enter(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(2)
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(u'\ue007')

    """чтобы очистить поле поиска, отправить другой ключ в поле поиска и нажатие клавишы ENTER"""
    def clear_text_in_element_and_send_text_with_enter(self, element, text):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().pause(2)
        element.clear()
        element.send_keys(text)
        element.send_keys(u'\ue007')

    """чтобы получить текст в элементе"""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """чтобы проверить, что элемент виден"""
    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """чтобы проверить, что элементы видны"""
    def are_visible(self, by_locator) -> bool:
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return bool(elements)

    """чтобы проверить, что элемент НЕ виден"""
    def is_not_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    """чтобы проверить, что элемент НЕ виден"""

    def element_is_not_visible(self, by_element) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(by_element))
        return bool(element)

    """чтобы проверить, что элемент виден"""

    def element_is_visible(self, by_element) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of(by_element))
        return bool(element)

    """ получить заголовок загруженной страницы"""
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    """найти один элемент"""
    def find_one_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    """найти несколько элементов"""
    def find_several_element(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return elements

    """для отображения подменю"""
    def move_to_show_submenu(self, by_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()

    """чтобы отобразить подменю и щелкнуть элемент на первом уровне"""
    def move_to_submenu_and_click_at_first_level(self, by_locator, submenu_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()
        submenu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submenu_locator))
        submenu.click()

    """чтобы отобразить подменю и перейти к элементу на первом уровне и щелкнуть элемент на втором уровне"""
    def move_to_submenu_and_click_at_second_level(self, by_locator, submenu_locator, second_level_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()
        submenu = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(submenu_locator))
        action.move_to_element(submenu).perform()
        second_level_submenu = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(second_level_locator))
        second_level_submenu.click()


    """получить атрибут элемента"""
    def get_attribute_value(self, by_locator, attr_name):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        value = element.get_attribute(attr_name)
        return value

    """прокрутить в поле зрения"""
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """этот метод принимает политику использования файлов cookie 
    и закрывает всплывающее окно, если оно отображается"""
    def accept_cookies_policy(self):
        if self.is_visible(COOKIES_POLICY_BUTTON):
            self.do_click(COOKIES_POLICY_BUTTON)
        else:
            pass

    """функция используется для обновления текущей открытой страницы"""
    def refresh_current_url(self):
        self.driver.get(self.driver.current_url)
        self.driver.refresh()

    """ Возвращает URL текущего браузера. """
    def get_current_url(self):
        return self.driver.current_url


