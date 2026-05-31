from selenium.webdriver.common.by import By

class ExceptionPageLocators:
    EXCEPTION_PAGE_URL = "https://practicetestautomation.com/practice-test-exceptions/"
    ADD_BUTTON = (By.ID, "add_btn")
    REMOVE_BUTTON = (By.ID, "remove_btn")
    EDIT_BUTTON = (By.ID, "edit_btn")
    SAVE_BUTTON = (By.NAME, "Save") # there are multiple Save buttons, we will handle this in the page class
    INPUT_FIELD1 = (By.XPATH, "//div[@id='row1']//input[@class='input-field']")
    INPUT_FIELD2 = (By.XPATH, "//div[@id='row2']//input[@class='input-field']")

