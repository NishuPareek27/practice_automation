from selenium.webdriver.support.ui import Select
from locators.tablepage_locators import TablePageLocators
from selenium.common.exceptions import *

class TablePracticePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators imported from TablePageLocators Class
    table_test_page = TablePageLocators.TEST_TABLE_PAGE_URL
    language_filter = TablePageLocators.LANGUAGE_FILTER
    course_language_cells = TablePageLocators.COURSE_LANGUAGE_CELLS
    level_filter = TablePageLocators.LEVEL_FILTER
    course_level_cells = TablePageLocators.COURSE_LEVEL_CELLS
    enrollment_filter = TablePageLocators.ENROLLMENT_FILTER
    enrollment_options = TablePageLocators.ENROLLMENT_OPTIONS
    course_enrollment_cells = TablePageLocators.COURSE_ENROLLMENT_CELLS


# Open the table practice page
    def open(self):
        self.driver.get(self.table_test_page)



# Course Language filter methods 
    def apply_lang_filter(self, filter_value):

        # We need to format the locator with the specific filter value (e.g., "Java", "Python", "Any")
        language_locator = (
            self.language_filter[0], # By.XPATH
            self.language_filter[1].format(filter_value=filter_value) # This will replace {filter_value} in the XPath with the actual filter value passed to the method
        )
        language_element = self.driver.find_element(*language_locator)

        try:                # Attempt to click the element normally
            language_element.click()
        
        except ElementNotInteractableException:             # If the element is not interactable, we use JavaScript to click it(coz it bypass the normal click method)
            self.driver.execute_script("arguments[0].click();", language_element)
    
    def get_course_languages(self):
            rows = self.driver.find_elements(*self.course_language_cells)

            # Return the text of each visible cell in the "Language" column
            # We check if the cell is displayed to ensure we only return languages that are currently visible after applying the filter
            # strip() is used to remove any leading/trailing whitespace from the text
            # This method will return a list of languages that are currently visible in the "Language" column of the table after applying the filter.
            return [row.text.strip() for row in rows if row.is_displayed()]

    
    
    
    
    
# Course Level filter methods 
    def apply_level_filter(self, level_filter_value):
                # # If a level filter value is provided (e.g., "Beginner"), we skip this filter, and we uncheck other filters
            # if level_filter_value == "Beginner":
            #     level_locator = (
            #         TablePageLocators.LEVEL_FILTER[0],
            #         TablePageLocators.LEVEL_FILTER[1].format(level_filter_value=level_filter_value)
            #     )
            #     level_element = self.driver.find_element(*level_locator)
            #     if level_element.is_selected():
            #         # Uncheck "Intermediate" and "Advanced" filters if they are checked
            #         for other_level in ["Intermediate", "Advanced"]:
            #             other_level_locator = (
            #                 TablePageLocators.LEVEL_FILTER[0],
            #                 TablePageLocators.LEVEL_FILTER[1].format(level_filter_value=other_level)
            #             )
            #             other_level_element = self.driver.find_element(*other_level_locator)
            #             if other_level_element.is_selected():
            #                 try:
            #                     other_level_element.click()
            #                 except ElementNotInteractableException:
            #                     self.driver.execute_script("arguments[0].click();", other_level_element)
            # else:
            #     try:
            #         if not level_element.is_selected():
            #             beginner_element = self.driver.find_element(*level_locator)
            #             beginner_element.click()
            #     except ElementNotInteractableException:
            #         self.driver.execute_script("arguments[0].click();", beginner_element)

            all_levels = ["Beginner", "Intermediate", "Advanced"]
            # We loop through all levels and check/uncheck them based on the provided level_filter_value
            for level in all_levels:
                locator = (
                    self.level_filter[0],
                    self.level_filter[1].format(level_filter_value=level)
                )
                element = self.driver.find_element(*locator)
                # If the current level in the loop matches the level filter value we want to apply, we make sure it's checked. For all other levels, we make sure they are unchecked.
                if level == level_filter_value:
                    # Make sure the level we want is checked
                    if not element.is_selected():
                        try:
                            element.click()
                        except ElementNotInteractableException:
                            self.driver.execute_script("arguments[0].click();", element)
                else:
                    # Uncheck all other levels
                    if element.is_selected():
                        try:
                            element.click()
                        except ElementNotInteractableException:
                            self.driver.execute_script("arguments[0].click();", element)
    
    def get_course_levels(self):
         rows = self.driver.find_elements(*self.course_level_cells)
         return [row.text.strip() for row in rows if row.is_displayed()]
    

    
    
    


# Enrollment filter methods 
    def apply_min_enrollment_filter(self, enrollment_value):
         # Click the enrollment filter dropdown to open it
        enrollment_filter_element = self.driver.find_element(*self.enrollment_filter)
        enrollment_filter_element.click()

        # Select the specified enrollment option from the dropdown
        enrollment_option_locator = (
            self.enrollment_options[0],
            self.enrollment_options[1].format(enrollment_value=enrollment_value)
        )
        enrollment_option_element = self.driver.find_element(*enrollment_option_locator)
        enrollment_option_element.click()


    def get_course_enrollments(self):
        enrollment_list=[]
        enrollment_cells = self.driver.find_elements(*self.course_enrollment_cells)
        # print([cell.text for cell in enrollment_cells])
        # print([cell.text.strip() for cell in enrollment_cells if cell.is_displayed()])
        enrollment_cells_list = [cell.text.strip() for cell in enrollment_cells if cell.is_displayed()]
        for enrollment in enrollment_cells_list:
            # Remove commas from the enrollment number and convert it to an integer for comparison
            enrollment_list.append(int(enrollment.replace(",", "")))

        # print(enrollment_list)
        return enrollment_list        
    

    def get_no_matching_courses_message(self):
        return self.driver.find_element(*TablePageLocators.NO_MATCHING_COURSES_MESSAGE)
    



    # Reset filters method
    def click_reset_filters(self):
        reset_button = self.driver.find_element(*TablePageLocators.RESET_FILTERS_BUTTON)
        assert reset_button.is_displayed() and reset_button.is_enabled(), "Reset Filters button is not visible or not enabled"
        reset_button.click()

    # Additional helper methods for assertions in tests
    def is_reset_button_hidden(self):
        reset_button = self.driver.find_element(*TablePageLocators.RESET_FILTERS_BUTTON)
        return not reset_button.is_displayed()
    
    # This method checks if the "Any" option is selected in the language filter and that "Java" and "Python" are not selected, which would indicate that the filters have been reset to their default state.
    def is_language_reset_to_any(self):
        # Check Any is selected
        any_locator = (
            TablePageLocators.LANGUAGE_FILTER[0],
            TablePageLocators.LANGUAGE_FILTER[1].format(filter_value="Any")
        )
        any_element = self.driver.find_element(*any_locator)
        if not any_element.is_selected():
            print("'Any' language filter is not selected after reset")
            return False

        # Check Java and Python are NOT selected
        for language in ["Java", "Python"]:
            locator = (
                TablePageLocators.LANGUAGE_FILTER[0],
                TablePageLocators.LANGUAGE_FILTER[1].format(filter_value=language)
            )
            element = self.driver.find_element(*locator)
            if element.is_selected():
                print(f"'{language}' filter is still selected after reset — expected it to be deselected")
                return False

        return True  # Any is selected and Java/Python are deselected
    
    # This method checks if all three level options ("Beginner", "Intermediate", "Advanced") are selected, which would indicate that the filters have been reset to their default state where all levels are included.
    def are_all_levels_checked(self):
        for level in ["Beginner", "Intermediate", "Advanced"]:
            locator = (
                TablePageLocators.LEVEL_FILTER[0],
                TablePageLocators.LEVEL_FILTER[1].format(level_filter_value=level)
            )
            element = self.driver.find_element(*locator)
            if not element.is_selected():
                # If any level is unchecked after reset — fail
                print(f"'{level}' is unchecked after reset — expected all levels to be checked")
                return False
        return True  # All 3 levels are checked
    
    # This method checks if the "Any" option is selected in the level filter and that "Beginner", "Intermediate", and "Advanced" are not selected, which would indicate that the filters have been reset to their default state.
    def is_enrollment_reset_to_any(self):
        # Check Any is selected
        any_locator = (
            TablePageLocators.ENROLLMENT_OPTIONS[0],
            TablePageLocators.ENROLLMENT_OPTIONS[1].format(enrollment_value="any")
        )
        any_element = self.driver.find_element(*any_locator)
        # if not any_element.is_selected():
        #     print("'Any' enrollment filter is not selected after reset")
        #     return False
        print(f"Any aria-selected value: {any_element.get_attribute('aria-selected')}")


        # Check other options are NOT selected
        for enrollment in ["5000", "10000", "50000"]:
            locator = (
                TablePageLocators.ENROLLMENT_OPTIONS[0],
                TablePageLocators.ENROLLMENT_OPTIONS[1].format(enrollment_value=enrollment)
            )
            element = self.driver.find_element(*locator)
            # print statement to show the aria-selected value for debugging purposes
            # if it is true, it means the option is still selected after reset, which would indicate that the reset did not work correctly for that option.
            print(f"{enrollment} aria-selected value: {element.get_attribute('aria-selected')}")
            if element.get_attribute("aria-selected") == "true":
                print(f" {enrollment} is still selected after reset")
                return False

        print(" Enrollment reset to Any successfully")
        return True

    def are_all_courses_visible(self):
        # This method checks if there are any courses visible in the table by checking if there are any visible language cells. If there are visible language cells, we can assume that courses are visible.
        visible_languages = self.get_course_languages()
        return len(visible_languages) > 0
    




# This method sorts the courses by enrollment in By-default ascending order by interacting with the sort dropdown menu. It creates a Select object for the sort filter element and selects the option corresponding to sorting by enrollment. The position parameter allows us to specify which option to select based on its index in the dropdown.
    def apply_sort_by(self, text):
        sort_filter = self.driver.find_element(*TablePageLocators.SORT_BY_FILTER)
        # We create a Select object using the sort filter element, which allows us to interact with the dropdown menu. We then use the select_by_value method to select the option with the value "col_enroll", which corresponds to sorting by enrollment in ascending order.
        select = Select(sort_filter)

        # These 3 ways to select options are interchangeable, we can use any of them to select the "Enrollments" option from the dropdown. In this case, we are using select_by_index(4) assuming that the "Enrollments" option is the 5th option in the dropdown (index starts at 0).
        select.select_by_visible_text(text)


    def get_course_names(self):
        name_cells = self.driver.find_elements(*TablePageLocators.COURSE_NAME_CELLS)
        return [cell.text.strip() for cell in name_cells if cell.is_displayed()]

