import locators


class TestRegistration:

    def test_successful_registration(self, driver, random_email, random_password):
        locators.click_to_lk_button(driver)
        locators.click_registration_link(driver)
        locators.set_name(driver)
        locators.set_random_login(driver, random_email)
        locators.set_random_password(driver, random_password)
        locators.click_to_registration_button(driver)
        assert locators.wait_for_login_text(driver) == "Вход"

    def test_incorrect_password_error(self, driver):
        locators.click_to_lk_button(driver)
        locators.click_registration_link(driver)
        locators.set_name(driver)
        locators.set_default_login(driver)
        locators.set_incorrect_password(driver)
        locators.click_to_registration_button(driver)
        assert locators.wait_for_incorrect_password_text(driver) == 'Некорректный пароль'

