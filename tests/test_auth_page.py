import allure
import pytest

from page_objects.BOPage import BOPage
from page_objects.BackOfficeSiginForm import BackOfficeSigninForm
from page_objects.MainPage import MainPage


def sign_bo(browser):
    MainPage(browser)._go_backoffice_page()
    BackOfficeSigninForm(browser).sign_in(email='pisecka.karina@gmail.com',
                                          password='karina1990')


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("demo_mode_toggle")
def test_demo_toggle(browser):
    sign_bo(browser)
    demo_toggle = BOPage(browser).click_demo_toggle()
    assert demo_toggle


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("demo_mode_toggle")
def test_demo_toggle(browser):
    sign_bo(browser)
    demo_toggle = BOPage(browser).click_demo_toggle()
    assert demo_toggle


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("orders")
def test_orders(browser):
    sign_bo(browser)
    orders = BOPage(browser).click_orders()
    assert orders


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("search")
def test_search(browser):
    sign_bo(browser)
    search = BOPage(browser).click_search()
    assert search


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("datepicker")
def test_datepicker(browser):
    sign_bo(browser)
    datepicker = BOPage(browser).click_datepicker()
    assert datepicker


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("month_period")
def test_month_period(browser):
    sign_bo(browser)
    month_period = BOPage(browser).click_month_period()
    assert month_period


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("refresh")
def test_refresh(browser):
    sign_bo(browser)
    refresh = BOPage(browser).click_refresh()
    assert refresh


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("configuration")
def test_config(browser):
    sign_bo(browser)
    config = BOPage(browser).click_config()
    assert config


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("customer notifications")
def test_notifications(browser):
    sign_bo(browser)
    notifications = BOPage(browser).click_notifications()
    assert notifications


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("official documentation")
def test_official_documentation(browser):
    sign_bo(browser)
    official_documentation = BOPage(browser).click_official_documentation()
    assert official_documentation


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("most viewed products")
def test_most_viewed(browser):
    sign_bo(browser)
    most_viewed = BOPage(browser).click_most_viewed()
    assert most_viewed


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("product conversion")
def test_conversion(browser):
    sign_bo(browser)
    conversion = BOPage(browser).click_conversion()
    assert conversion


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("search a product")
def test_search(browser):
    sign_bo(browser)
    search = BOPage(browser).click_search()
    assert search


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Localization")
def test_localization(browser):
    sign_bo(browser)
    localization = BOPage(browser).click_localization()
    assert localization


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Customers")
def test_customers(browser):
    sign_bo(browser)
    customers = BOPage(browser).click_customers()
    assert customers


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Dashboard")
def test_dashboard(browser):
    sign_bo(browser)
    dashboard = BOPage(browser).click_dashboard()
    assert dashboard


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Top Searches")
def test_top_search(browser):
    sign_bo(browser)
    top_search = BOPage(browser).click_top_search()
    assert top_search


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Contact Us")
def test_contacts(browser):
    sign_bo(browser)
    contacts = BOPage(browser).click_contacts()
    assert contacts


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Add Ons")
def test_add_ons(browser):
    sign_bo(browser)
    add_ons = BOPage(browser).click_add_ons()
    assert add_ons


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Link Google Analytics")
def test_google_analytics(browser):
    sign_bo(browser)
    google_analytics = BOPage(browser).click_google_analytics()
    assert google_analytics


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Online Visitors")
def test_online_visitors(browser):
    sign_bo(browser)
    online_visitors = BOPage(browser).click_online_visitors()
    assert online_visitors


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Create account in the BO")
def test_create_account(browser):
    sign_bo(browser)
    BOPage(browser).click_menu_customer()
    BOPage(browser).click_button_add_customer()
    BOPage(browser).fill_customer_create_form(firstname='Antonio',
                                              lastname='Chehov',
                                              email='chehov5@gmail.com',
                                              password='anton123')
    alert_success = BOPage(browser).get_alert_success()
    assert alert_success == '×\nSuccessful creation'


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Create account in the BO and create duplicate ")
def test_create_account_and_create_duplicate(browser):
    sign_bo(browser)
    email = 'ant@gmail.com'
    for i in range(2):
        BOPage(browser).click_menu_customer()
        BOPage(browser).click_button_add_customer()
        BOPage(browser).fill_customer_create_form(firstname='Ann',
                                                  lastname='T',
                                                  email=email,
                                                  password='ant123')
    alert_failed = BOPage(browser).get_alert_success()
    assert alert_failed == f'×\nAn account already exists for this email address: {email}'


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Create account in the BO and sign in with new register account in the App ")
@pytest.mark.parametrize("firstname,email,password",
                         [('Alisa', 'alice22@gmail.com', 'alice123'),
                          ('Mary', 'mary22@gmail.com', 'mary123')
                          ])
def test_create_account_and_sigin(browser):
    sign_bo(browser)
    firstname = 'Alisa'
    email = 'alice555@gmail.com'
    password = 'alice123'
    BOPage(browser).click_menu_customer()
    BOPage(browser).click_button_add_customer()
    BOPage(browser).fill_customer_create_form(firstname=firstname,
                                              lastname='Lastname',
                                              email=email,
                                              password=password)
    BOPage(browser)._go_to_main_page()
    MainPage(browser).click_sign_in()
    MainPage(browser).fill_sign_in_form(email=email, password=password)
    customer_name = MainPage(browser).check_customer_name()
    assert customer_name == firstname


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("Create account in the BO and sign in with new register account in the App ")
@pytest.mark.xfail
def test_create_account_and_sigin_failed(browser):
    sign_bo(browser)
    firstname = 'Alisa'
    email = 'alice@gmail.com'
    password = 'alice123'
    BOPage(browser).click_menu_customer()
    BOPage(browser).click_button_add_customer()
    BOPage(browser).fill_customer_create_form(firstname=firstname,
                                              lastname='Eagle',
                                              email=email,
                                              password=password)
    BOPage(browser)._go_to_main_page()
    MainPage(browser).click_sign_in()
    MainPage(browser).fill_sign_in_form(email=email, password=password)
    customer_name = MainPage(browser).check_customer_name()
    assert customer_name == firstname


@allure.suite('BOPage')
@allure.epic("2022Q2")
@allure.feature("BOPage")
@allure.story("search a customer")
@pytest.mark.parametrize("search_input", ['Anton', 'Ann', 'Alisa'])
def test_search_customer(browser, search_input):
    sign_bo(browser)
    result_search = BOPage(browser).search_customer(search_input)
    assert f'your query "{search_input}"' in result_search
