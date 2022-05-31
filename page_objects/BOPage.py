from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from .BasePage import BasePage
from .CustomerCreateForm import CustomerCreateForm


class BOPage(BasePage):
    DEMO_TOGGLE = (By.ID, 'page-header-desc-configuration-switch_demo')
    ORDERS = (By.XPATH, '//*[@id="maintab-AdminParentOrders"]/a')
    SEARCH = (By.ID, 'bo_query')
    DATEPICKER = (By.ID, 'datepicker-from-info')
    MONTH_PERIOD = (By.XPATH, '//*[@id="calendar_form"]/div[1]/button[2]')
    REFRESH = (By.XPATH, '//*[@id="dashactivity"]/div/span/a[2]')
    CONFIGURATION = (By.XPATH, '//*[@id="dashactivity"]/div/span/a[1]')
    NOTIFICATIONS = (By.ID, 'customers_notif')
    OFFICIAL_DOCUMENTATION = (By.XPATH, '//*[@id="dashboard"]/div[2]/div[3]/section/dl[1]/dt/a')
    MOST_VIEWED = (By.XPATH, '//*[@id="dashproducts"]/section[2]/nav/ul/li[3]/a')
    CONVERSION = (By.XPATH, '//*[@id="dashgoals"]/section[2]/div[1]/label[2]')
    SEARCH = (By.ID, 'search_type_icon')
    LOCALIZATION = (By.XPATH, '//*[@id="maintab-AdminParentLocalization"]/a')
    CUSTOMERS = (By.XPATH, '//*[@id="maintab-AdminParentCustomer"]/a')
    DASHBOARD = (By.XPATH, '//*[@id="maintab-AdminDashboard"]/a')
    TOP_SEARCH = (By.XPATH, '//*[@id="dashproducts"]/section[2]/nav/ul/li[4]/a')
    CONTACTS = (By.XPATH, '//*[@id="dashboard"]/div[2]/div[3]/section/dl[4]/dt/a')
    ADDONS = (By.XPATH, '//*[@id="dashboard"]/div[2]/div[3]/section/dl[3]/dt/a')
    GOOGLE_ANALYTICS = (By.XPATH, '//*[@id="dash_traffic"]/ul/li[1]/span/a')
    ONLINE_VISITORS = (By.XPATH, '//*[@id="dash_live"]/ul/li[1]/span[1]/a')
    BUTTON_ADD_CUSTOMER = (By.ID, 'page-header-desc-customer-new_customer')
    ALERT_SUCCESS = (By.XPATH, '//*[@id="content"]/div[3]/div')
    RESULT_SEARCH = (By.XPATH, '//*[@id="content"]/div[5]/div/h2')
    SEARCH = (By.ID, 'bo_query')

    def click_demo_toggle(self):
        demo_toggle = self._element(self.DEMO_TOGGLE)
        self._simple_click_element(demo_toggle)
        return demo_toggle

    def click_orders(self):
        orders = self._element(self.ORDERS)
        self._simple_click_element(orders)
        return orders

    def click_search(self):
        search = self._element(self.SEARCH)
        self._simple_click_element(search)
        return search

    def click_datepicker(self):
        datepicker = self._element(self.DATEPICKER)
        self._simple_click_element(datepicker)
        return datepicker

    def click_month_period(self):
        month_period = self._element(self.MONTH_PERIOD)
        self._simple_click_element(month_period)
        return month_period

    def click_refresh(self):
        refresh = self._element(self.REFRESH)
        self._simple_click_element(refresh)
        return refresh

    def click_config(self):
        config = self._element(self.CONFIGURATION)
        self._simple_click_element(config)
        return config

    def click_notifications(self):
        notifications = self._element(self.NOTIFICATIONS)
        self._simple_click_element(notifications)
        return notifications

    def click_official_documentation(self):
        official_documentation = self._element(self.OFFICIAL_DOCUMENTATION)
        self._simple_click_element(official_documentation)
        return official_documentation

    def click_most_viewed(self):
        most_viewed = self._element(self.MOST_VIEWED)
        self._simple_click_element(most_viewed)
        return most_viewed

    def click_conversion(self):
        conversion = self._element(self.CONVERSION)
        self._simple_click_element(conversion)
        return conversion

    def click_search(self):
        search = self._element(self.SEARCH)
        self._simple_click_element(search)
        return search

    def click_localization(self):
        localization = self._element(self.LOCALIZATION)
        self._simple_click_element(localization)
        return localization

    def click_customers(self):
        customers = self._element(self.CUSTOMERS)
        self._simple_click_element(customers)
        return customers

    def click_dashboard(self):
        dashboard = self._element(self.DASHBOARD)
        self._simple_click_element(dashboard)
        return dashboard

    def click_top_search(self):
        top_search = self._element(self.TOP_SEARCH)
        self._simple_click_element(top_search)
        return top_search

    def click_contacts(self):
        contacts = self._element(self.CONTACTS)
        self._simple_click_element(contacts)
        return contacts

    def click_add_ons(self):
        add_ons = self._element(self.ADDONS)
        self._simple_click_element(add_ons)
        return add_ons

    def click_google_analytics(self):
        google_analytics = self._element(self.GOOGLE_ANALYTICS)
        self._simple_click_element(google_analytics)
        return google_analytics

    def click_online_visitors(self):
        online_visitors = self._element(self.ONLINE_VISITORS)
        self._simple_click_element(online_visitors)
        return online_visitors

    def click_menu_customer(self):
        menu_customer = self._element(self.CUSTOMERS)
        self._simple_click_element(menu_customer)
        return menu_customer

    def click_button_add_customer(self):
        button_add_customer = self._element(self.BUTTON_ADD_CUSTOMER)
        self._simple_click_element(button_add_customer)
        return button_add_customer

    def fill_customer_create_form(self, firstname, lastname, email, password):
        CustomerCreateForm(self.browser).create_customer(firstname, lastname, email, password)

    def get_alert_success(self):
        alert_success = self._element(self.ALERT_SUCCESS).text.strip()
        return alert_success

    def search_customer(self, name_customer):
        self._element(self.SEARCH).send_keys(name_customer)
        self._element(self.SEARCH).send_keys(Keys.RETURN)
        result = self._element(self.RESULT_SEARCH).text

        return result
