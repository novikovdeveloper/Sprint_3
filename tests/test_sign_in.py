import locators


class TestSignIn:
    def test_sign_in_on_main_page(self, driver):
        locators.click_sign_in_to_account(driver)
        locators.wait_for_login_text(driver)
        locators.login_with_default_data(driver)
        assert locators.wait_for_burger_page_text(driver) == "Соберите бургер"

    def test_sign_in_by_lk_button(self, driver):
        locators.click_to_lk_button(driver)
        locators.login_with_default_data(driver)
        assert locators.wait_for_burger_page_text(driver) == "Соберите бургер"

    def test_sign_in_by_registration_form(self, driver):
        locators.click_to_lk_button(driver)
        locators.click_to_register_button(driver)
        locators.click_to_login_link(driver)
        locators.login_with_default_data(driver)
        assert locators.wait_for_burger_page_text(driver) == "Соберите бургер"

    def test_sign_in_by_reset_password_form(self, driver):
        locators.click_to_lk_button(driver)
        locators.click_to_reset_password_button(driver)
        locators.click_to_login_link(driver)
        locators.login_with_default_data(driver)
        assert locators.wait_for_burger_page_text(driver) == "Соберите бургер"