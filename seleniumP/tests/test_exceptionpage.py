from locators.exceptionpage_locators import ExceptionPageLocators
from seleniumP.pages.exception_practicepage import ExceptionPracticePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import * 


def test_check_nosuchelement_exception(driver):
    exception_page = ExceptionPracticePage(driver)
    exception_page.open()
    exception_page.click_add()
    
    # Wait for the new field to be added to the DOM (check presence first)
    field2 = Wait(driver, 10).until(
        EC.visibility_of_element_located(ExceptionPageLocators.INPUT_FIELD2)
    )

    assert field2.is_displayed(), "Input Field 2 should be visible after clicking Add button"
    # exception_page.enter_text_in_field2("Testing NoSuchElementException")


def test_element_not_interactable_exception(driver):
    exception_page = ExceptionPracticePage(driver)
    exception_page.open()
    exception_page.click_add()
    
    # Wait for the new field to be added to the DOM (check presence first)
    Wait(driver, 10).until(
        EC.visibility_of_element_located(ExceptionPageLocators.INPUT_FIELD2)
    )
    
    exception_page.enter_text_in_field2("Testing ElementNotInteractableException by adding this Text to the input_field2")
    exception_page.click_save()


def test_invalid_element_state_exception(driver):
    exception_page = ExceptionPracticePage(driver)

    test_text = (
        "Testing InvalidElementStateException by adding this Text "
        "to the input_field1 via Nishu Pareek"
    )

    exception_page.open()
    exception_page.click_edit()

    exception_page.clear_text_in_field1()
    exception_page.enter_text_in_field1(test_text)

    exception_page.click_save()

    # Verify updated text
    field1_value = driver.find_element(
        *ExceptionPageLocators.INPUT_FIELD1
    ).get_attribute("value")

    assert field1_value == test_text, (
        "Input Field 1 should have the updated text "
        "after clicking Save button"
    )


def test_check_stale_element_reference_exception(driver):
    exception_page = ExceptionPracticePage(driver)
    exception_page.open()

    instruction_text = driver.find_element(By.XPATH, "//p[@id='instructions']")
    assert instruction_text.is_displayed(), "Instruction text should be visible on the page"
    exception_page.click_add()

    try:
        instruction_text.is_displayed()  # This should raise StaleElementReferenceException
        assert False, "Expected StaleElementReferenceException was not raised"
    except StaleElementReferenceException:
        pass  # Test passes if exception is raised