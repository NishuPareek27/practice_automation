from seleniumP.pages.login_page import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("student", "Password123")

    assert "Logged In Successfully" in login.get_success_text()


def test_invalid_username(driver):
    login = LoginPage(driver)
    login.open()
    login.login("wrongUser", "Password123")

    assert "Your username is invalid!" in login.get_error_text()


def test_invalid_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("student", "wrongPass")

    assert "Your password is invalid!" in login.get_error_text()