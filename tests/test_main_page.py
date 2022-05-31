import allure
import pytest

from page_objects.AuthenticationPage import AuthenticationPage
from page_objects.MainPage import MainPage


def sign_in_user(browser):
    MainPage(browser).click_sign_in()
    MainPage(browser).fill_sign_in_form(email='pisecka.karina@gmail.com',
                                        password='karina1990')
    MainPage(browser)._go_to_main_page()


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("book_now")
def test_book_now(browser):
    book_now = MainPage(browser).click_book_now()
    assert book_now


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("search_button")
def test_search_button(browser):
    search_button = MainPage(browser).click_search_button()
    assert search_button


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("menu")
def test_menu(browser):
    menu = MainPage(browser).click_menu()
    assert menu


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("signin")
def test_sign_in(browser):
    sign_in = MainPage(browser).click_sign_in()
    assert sign_in


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("booking cart")
def test_cart(browser):
    cart = MainPage(browser).click_cart()
    assert cart


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("booking cart")
def test_cart(browser):
    cart = MainPage(browser).click_cart()
    assert cart


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("subscribe")
def test_subscribe(browser):
    subscribe = MainPage(browser).click_subscribe()
    assert subscribe


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("facebook")
def test_facebook(browser):
    facebook = MainPage(browser).click_facebook()
    assert facebook


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("gmail")
def test_gmail(browser):
    gmail = MainPage(browser).click_gmail()
    assert gmail


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("languages")
def test_languages(browser):
    languages = MainPage(browser).click_languages()
    assert languages


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("about us")
def test_about_us(browser):
    about_us = MainPage(browser).click_about_us()
    assert about_us


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("secure pay")
def test_secure_pay(browser):
    secure_pay = MainPage(browser).click_secure_pay()
    assert secure_pay


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("terms and conditions")
def test_terms(browser):
    terms = MainPage(browser).click_terms()
    assert terms


@allure.suite('MainPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("legal notice")
def test_legal(browser):
    legal = MainPage(browser).click_legal()
    assert legal


@allure.suite('AuthenticationPage')
@allure.epic("2022Q2")
@allure.feature("AuthenticationPage")
@allure.story("register_account")
@pytest.mark.skip
def test_register_account(browser):
    MainPage(browser).go_to_authentication_page()
    register_account = AuthenticationPage(browser).enter_email(email='pisecka.karina@gmail.com')
    assert register_account


@allure.suite('AuthenticationPage')
@allure.epic("2022Q2")
@allure.feature("AuthenticationPage")
@allure.story("sign_in_account")
@pytest.mark.skip
def test_sign_in_account(browser):
    MainPage(browser).go_to_authentication_page()
    sign_in_account = AuthenticationPage(browser).sign_in_account(email='pisecka.karina@gmail.com',
                                                                  password='karina1990')
    assert sign_in_account


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("MainPage")
@allure.story("book a room")
@pytest.mark.xfail
def test_book_room(browser):
    sign_in_user(browser)
    MainPage(browser).click_book_now2()
    MainPage(browser).click_reserve_room()
    result = MainPage(browser).get_reserve_room_result()
    assert 'SyntaxError' in result
