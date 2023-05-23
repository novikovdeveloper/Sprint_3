import locators


class TestLogout:
    def test_logout_from_lk(self, driver):
        # клик по кнопке "Войти в аккаунт"
        locators.click_sign_in_to_account(driver)
        locators.login_with_default_data(driver)
        locators.click_to_lk_button(driver)
        locators.wait_for_account_profile_page_text(driver)
        locators.click_to_logout_button(driver)
        locators.wait_for_login_text(driver)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'