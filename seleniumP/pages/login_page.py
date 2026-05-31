from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators imported from LoginLocators Class
    username = LoginLocators.USERNAME
    password = LoginLocators.PASSWORD
    submit_btn = LoginLocators.SUBMIT_BTN
    error_msg = LoginLocators.ERROR_MSG
    success_msg = LoginLocators.SUCCESS_MSG

    # Actions
    def open(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.submit_btn).click()

    # Validations
    def get_error_text(self):
        return self.driver.find_element(*self.error_msg).text

    def get_success_text(self):
        return self.driver.find_element(*self.success_msg).text