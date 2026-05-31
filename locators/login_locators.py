from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT_BTN = (By.ID, "submit")
    ERROR_MSG = (By.ID, "error")
    SUCCESS_MSG = (By.CLASS_NAME, "post-title")