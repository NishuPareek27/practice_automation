from selenium.webdriver.common.by import By

class TablePageLocators:
    TEST_TABLE_PAGE_URL = "https://practicetestautomation.com/practice-test-table/"

    LANGUAGE_FILTER = (By.XPATH, "//input[@type='radio' and @value='{filter_value}']")
    COURSE_LANGUAGE_CELLS = (By.XPATH, "//table//tr/td[3]")

    LEVEL_FILTER = (By.XPATH, "//input[@type='checkbox' and @name='level' and @value='{level_filter_value}']")
    COURSE_LEVEL_CELLS = (By.XPATH, "//table//tr/td[4]")

    ENROLLMENT_FILTER = (By.XPATH, "//div[@class='dropdown']")
    ENROLLMENT_OPTIONS = (By.XPATH, "//li[@data-value='{enrollment_value}']")
    COURSE_ENROLLMENT_CELLS = (By.XPATH, "//table//tr/td[5]")

    NO_MATCHING_COURSES_MESSAGE = (By.XPATH, "//div[contains(text(),'No matching courses')]")

    RESET_FILTERS_BUTTON = (By.XPATH, "//button[text()='Reset']")

    SORT_BY_FILTER = (By.XPATH, "//select[@id='sortBy']")
    SORT_BY_OPTIONS = (By.XPATH, "//select[@id='sortBy']/option[@value='{sort_value}']")


    COURSE_NAME_CELLS = (By.XPATH, "//table//tr/td[2]")

    