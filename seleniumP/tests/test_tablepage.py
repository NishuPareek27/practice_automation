import pytest
from seleniumP.pages.table_practicepage import TablePracticePage



# CASE 1: Verify only selected courses are visible
@pytest.mark.parametrize("filter_value", ["Java", "Python", "Any"])
def test_language_filter(driver, filter_value):
    
    table_page = TablePracticePage(driver)
    table_page.open()

    # Apply the specified filter and verify results
    table_page.apply_lang_filter(filter_value)

    visible_languages = table_page.get_course_languages()
    # Assert that there are visible languages after applying the specified filter
    assert len(visible_languages) > 0, f"No courses visible after applying {filter_value} filter"

    # If "Any" is selected, all languages should be visible
    if filter_value == "Any":
        assert set(visible_languages) == {"Java", "Python", "Any"}, (
            f"Expected all languages but got: {visible_languages}"
        )
    # Otherwise only the selected language should be visible
    else:
        for lang in visible_languages:
            assert lang == filter_value, (
                f"Expected '{filter_value}' but found '{lang}' after applying {filter_value} filter"
            )


# CASE 2: Verify only courses matching the selected level are visible
@pytest.mark.parametrize("level_value", ["Beginner", "Intermediate", "Advanced"])
def test_level_filter(driver, level_value):
    table_page = TablePracticePage(driver)
    table_page.open()

    # Apply the specified level filter and verify results
    table_page.apply_lang_filter("Any")
    table_page.apply_level_filter(level_value)

    visible_levels = table_page.get_course_levels()

    # Assert that there are visible levels after applying the specified filter
    assert len(visible_levels) > 0, f"No courses visible after applying {level_value} level filter"

    # Assert that all visible levels are the specified level
    for level in visible_levels:
        assert level == level_value, (
            f"Expected '{level_value}' but found '{level}' after applying {level_value} filter"
        )


# CASE 3: Verify only courses with the specified enrollment are visible
def test_enrollment_filter(driver):
    table_page = TablePracticePage(driver)
    table_page.open()

    # Apply the enrollment filter for "Full-time" and verify results
    table_page.apply_min_enrollment_filter("10000")

    visible_enrollments = table_page.get_course_enrollments()

    # Assert that there are visible enrollments after applying the filter
    assert len(visible_enrollments) > 0, "No courses visible after applying 10000+ enrollment filter"

    # Assert that all visible enrollments are "10000+"
    for enrollment in visible_enrollments:
        assert enrollment >= 10000, (
            f"Expected '10000+' but found '{enrollment}' after applying 10000+ enrollment filter"
        )


# CASE 4: Verify that applying multiple filters together works correctly and only courses matching all criteria are visible
def test_combined_filter_test(driver):
    table_page = TablePracticePage(driver)
    table_page.open()

    # Apply multiple filters and verify results
    table_page.apply_lang_filter("Python")
    table_page.apply_level_filter("Beginner")
    table_page.apply_min_enrollment_filter("10000")

    visible_languages = table_page.get_course_languages()
    visible_levels = table_page.get_course_levels()
    visible_enrollments = table_page.get_course_enrollments()

    # Assert that there are visible courses after applying the combined filters
    assert len(visible_languages) > 0, "No courses visible after applying combined filters"

    # # Assert that all visible courses match the combined filter criteria
    # for lang in visible_languages:
    #     assert lang == "Python", f"Expected 'Python' but found '{lang}' after applying combined filters"
    # for level in visible_levels:
    #     assert level == "Beginner", f"Expected 'Beginner' but found '{level}' after applying combined filters"
    # for enrollment in visible_enrollments:
    #     assert enrollment >= 10000, (
    #         f"Expected '10000+' but found '{enrollment}' after applying combined filters"
    #     )


    # zip() combines multiple lists row by row, so we can check the language, level, and enrollment for each visible course together    
    for lang, level, enrollment in zip(visible_languages, visible_levels, visible_enrollments):
        assert lang == "Python", f"Expected 'Python' but found '{lang}' after applying combined filters"
        assert level == "Beginner", f"Expected 'Beginner' but found '{level}' after applying combined filters"
        assert enrollment >= 10000, (
            f"Expected '10000+' but found '{enrollment}' after applying combined filters"
        )



# CASE 5: Verify that when filters are applied that yield no results, the appropriate message is displayed and no courses are visible
def test_no_results_after_filter(driver):
    table_page = TablePracticePage(driver)
    table_page.open()

    # Apply filters that are unlikely to yield results (e.g., "Python" + "Advanced")
    table_page.apply_lang_filter("Python")
    table_page.apply_level_filter("Advanced")
 

    visible_languages = table_page.get_course_languages()

    # Assert that no courses are visible after applying the filters
    assert len(visible_languages) == 0, "Expected no courses to be visible after applying filters but some courses are still visible"

    # Assert that the "No matching courses" message is displayed
    no_courses_message = table_page.get_no_matching_courses_message()
    assert no_courses_message.is_displayed(), "Expected 'No matching courses' message to be displayed but it is not visible"


# CASE 6: Verify that resetting filters works correctly and all courses are visible again
def test_reset_filters(driver):
    table_page = TablePracticePage(driver)
    table_page.open()

    # Apply some filters
    table_page.apply_lang_filter("Java")
    table_page.apply_level_filter("Intermediate")


    # Reset all filters
    table_page.click_reset_filters()


    assert table_page.is_language_reset_to_any(), "Language filter was not reset to 'Any'"
    assert table_page.are_all_levels_checked(), "Not all Levels are checked after reset"
    assert table_page.is_enrollment_reset_to_any(), "Enrollment filter was not reset to 'Any'"

    assert table_page.is_reset_button_hidden(), "Reset button should be hidden after clicking it but it is still visible"

    all_courses = table_page.are_all_courses_visible()  # Assuming this method returns the languages of all visible courses
    assert all_courses, "Expected all courses to be visible after resetting filters but no courses are visible"



# CASE 7: Verify that sorting by enrollment displays courses in the correct order (ascending)
def test_sort_by_enrollment_ascending(driver):
    table_page = TablePracticePage(driver)
    table_page.open()

    
    # Apply sorting by enrollment
    table_page.apply_sort_by("Enrollments")

    # Get the enrollments of the visible courses after sorting
    visible_enrollments = table_page.get_course_enrollments()

    # Assert that there are visible enrollments after applying the sorting
    assert len(visible_enrollments) > 0, "No courses visible after applying sorting by enrollment"

    # Assert that the enrollments are sorted in ascending order
    assert visible_enrollments == sorted(visible_enrollments), (
        f"Expected enrollments to be sorted in ascending order but got: {visible_enrollments}"
    )


# CASE 8: Verify that sorting by course name displays courses in the correct order (A→Z)
def test_sort_by_course_name_ascending(driver):
    table_page = TablePracticePage(driver)
    table_page.open()

    
    # Apply sorting by course name
    table_page.apply_sort_by("Course Name")

    # Get the course names of the visible courses after sorting
    visible_course_names = table_page.get_course_names()

    # Assert that there are visible course names after applying the sorting
    assert len(visible_course_names) > 0, "No courses visible after applying sorting by course name"

    assert visible_course_names == sorted(visible_course_names, key=lambda x: x.lower().strip()), (
        f"Expected A→Z order but got: {visible_course_names}"
    )
