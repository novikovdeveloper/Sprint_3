import locators


class TestTransitions:
    def test_transition_to_lk(self, driver):
        locators.click_sign_in_to_account(driver)
        locators.login_with_default_data(driver)
        locators.click_to_lk_button(driver)
        locators.wait_for_account_profile_page_text(driver)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_transition_from_lk_to_constructor(self, driver):
        locators.click_sign_in_to_account(driver)
        locators.login_with_default_data(driver)
        locators.click_to_lk_button(driver)
        locators.click_to_constructor_button(driver)
        assert locators.wait_for_burger_page_text(driver) == "Соберите бургер"

    def test_transition_to_constructor_and_burgers_logo(self, driver):
        locators.click_sign_in_to_account(driver)
        locators.login_with_default_data(driver)
        locators.click_to_lk_button(driver)
        locators.click_to_burgers_logo(driver)
        assert locators.wait_for_burger_page_text(driver) == "Соберите бургер"


