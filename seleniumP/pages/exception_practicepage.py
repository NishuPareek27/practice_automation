from locators.exceptionpage_locators import ExceptionPageLocators


class ExceptionPracticePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators imported from ExceptionPageLocators Class
    exception_page = ExceptionPageLocators.EXCEPTION_PAGE_URL
    add_button = ExceptionPageLocators.ADD_BUTTON
    remove_button = ExceptionPageLocators.REMOVE_BUTTON
    edit_button = ExceptionPageLocators.EDIT_BUTTON
    save_button = ExceptionPageLocators.SAVE_BUTTON
    input_field1 = ExceptionPageLocators.INPUT_FIELD1
    input_field2 = ExceptionPageLocators.INPUT_FIELD2

# Open the exception practice page
    def open(self):
        self.driver.get(self.exception_page)




# Methods to interact with the elements on the exception practice page
    def click_add(self):
        self.driver.find_element(*self.add_button).click()

    def click_remove(self):
        self.driver.find_element(*self.remove_button).click()

    def click_edit(self):
        self.driver.find_element(*self.edit_button).click()

    def click_save(self):
        buttons = self.driver.find_elements(*ExceptionPageLocators.SAVE_BUTTON)
        print(len(buttons))
        for btn in buttons:
            if btn.is_displayed() and btn.is_enabled():
                btn.click()
                return

        raise Exception("No visible Save button found")

    def enter_text_in_field1(self, text):
        self.driver.find_element(*self.input_field1).send_keys(text)

    def clear_text_in_field1(self):
        self.driver.find_element(*self.input_field1).clear()

    def enter_text_in_field2(self, text):
        self.driver.find_element(*self.input_field2).send_keys(text)