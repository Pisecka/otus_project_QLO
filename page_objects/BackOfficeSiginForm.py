from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class BackOfficeSigninForm(BasePage):
    EMAIL = (By.CSS_SELECTOR, "#email")
    PASSWORD = (By.CSS_SELECTOR, "#passwd")
    BUTTON_SIGN_IN = (By.XPATH, '//*[@id="login_form"]/div[3]/button')

    def sign_in(self, email, password):
        self.logger.info('Filling in BackOffice signin Form')
        self._element(self.EMAIL).send_keys(email)
        self._element(self.PASSWORD).send_keys(password)
        self._element(self.BUTTON_SIGN_IN).click()
