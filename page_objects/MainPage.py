from selenium.webdriver.common.by import By

from .BasePage import BasePage
from .SiginForm import SiginForm


class MainPage(BasePage):
    BOOK_NOW = (By.XPATH, '//*[@id="hotelRoomsBlock"]/div/div[2]/div/div[1]/div[1]/div/div[3]/a')
    SEARCH_BUTTON = (By.ID, 'search_room_submit')
    MENU = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[2]/button')
    SIGN_IN = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[7]/ul/li/a')
    CART = (By.XPATH, '// *[ @ id = "header"] / div[3] / div / div / div[4] / div / a')
    SUBSCRIBE = (By.XPATH, '//*[@id="footer"]/div/div[3]/div[1]/section/div[2]/form/div/button')
    FACEBOOK = (By.XPATH, '//*[@id="social_block"]/ul/li[1]/a')
    GMAIL = (By.XPATH, '//*[@id="social_block"]/ul/li[3]/a')
    LANGUAGES = (By.ID, 'languages-block-top')
    ABOUT_US = (By.XPATH, '//*[@id="footer"]/div/div[4]/div/section/div[2]/ul/li[4]/a')
    SECURE_PAY = (By.XPATH, '//*[@id="footer"]/div/div[4]/div/section/div[2]/ul/li[5]/a')
    TERMS = (By.XPATH, '//*[@id="footer"]/div/div[4]/div/section/div[2]/ul/li[3]/a')
    LEGAL = (By.XPATH, '//*[@id="footer"]/div/div[4]/div/section/div[2]/ul/li[2]/a')
    CUSTOMER_NAME = (By.XPATH, '//*[@id="user_info_acc"]/span[1]')
    BOOK_NOW2 = (By.XPATH, '//*[@id="hotelRoomsBlock"]/div/div[2]/div/div[2]/div[1]/div/div[3]/a')
    RESERVE_ROOM = (By.NAME, 'Submit')
    RESERVE_ROOM_RESULT = (By.XPATH, '//*[@id="product"]/div[3]/div/div/div/div/p[1]')

    def click_book_now(self):
        book_now = self._element(self.BOOK_NOW)
        self._simple_click_element(book_now)
        return book_now

    def click_search_button(self):
        search_button = self._element(self.SEARCH_BUTTON)
        self._simple_click_element(search_button)
        return search_button

    def click_menu(self):
        menu = self._element(self.MENU)
        self._simple_click_element(menu)
        return menu

    def click_sign_in(self):
        sign_in = self._element(self.SIGN_IN)
        self._simple_click_element(sign_in)
        return sign_in

    def click_cart(self):
        cart = self._element(self.CART)
        self._simple_click_element(cart)
        return cart

    def click_subscribe(self):
        subscribe = self._element(self.SUBSCRIBE)
        self._simple_click_element(subscribe)
        return subscribe

    def click_facebook(self):
        facebook = self._element(self.FACEBOOK)
        self._simple_click_element(facebook)
        return facebook

    def click_gmail(self):
        gmail = self._element(self.GMAIL)
        self._simple_click_element(gmail)
        return gmail

    def click_languages(self):
        languages = self._element(self.LANGUAGES)
        self._simple_click_element(languages)
        return languages

    def click_about_us(self):
        about_us = self._element(self.ABOUT_US)
        self._simple_click_element(about_us)
        return about_us

    def click_secure_pay(self):
        secure_pay = self._element(self.SECURE_PAY)
        self._simple_click_element(secure_pay)
        return secure_pay

    def click_terms(self):
        terms = self._element(self.TERMS)
        self._simple_click_element(terms)
        return terms

    def click_legal(self):
        legal = self._element(self.LEGAL)
        self._simple_click_element(legal)
        return legal

    def go_to_authentication_page(self):
        self.click_sign_in()

    def go_to_backoffice_page(self):
        self.click_sign_in()

    def fill_sign_in_form(self, email, password):
        SiginForm(self.browser).sign_in(email=email, password=password)

    def check_customer_name(self):
        customer_name = self._element(self.CUSTOMER_NAME).text
        return customer_name

    def click_book_now2(self):
        book_now2 = self._element(self.BOOK_NOW2)
        self._simple_click_element(book_now2)
        return book_now2

    def click_reserve_room(self):
        reserve_room = self._element(self.RESERVE_ROOM)
        self._simple_click_element(reserve_room)
        return reserve_room

    def get_reserve_room_result(self):
        reserve_room_result = self._element(self.RESERVE_ROOM_RESULT).text
        return reserve_room_result
