from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CustomerCreateForm(BasePage):
    TITLE = (By.ID, "gender_1")
    F_NAME = (By.ID, "firstname")
    L_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    BUTTON_SAVE = (By.ID, "customer_form_submit_btn")

    def create_customer(self, firstname, lastname, email, password):
        self.logger.info('Filling in Customer Create Form')
        self._element(self.TITLE).click()
        self._element(self.F_NAME).send_keys(firstname)
        self._element(self.L_NAME).send_keys(lastname)
        self._element(self.EMAIL).send_keys(email)
        self._element(self.PASSWORD).send_keys(password)
        self._element(self.BUTTON_SAVE).click()
