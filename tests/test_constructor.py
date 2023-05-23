import locators


class TestConstructor:
    def test_bun_section(self, driver):
        locators.click_sign_in_to_account(driver)
        locators.login_with_default_data(driver)
        locators.click_to_constructor_button(driver)
        locators.click_to_sauces_link(driver)
        locators.click_to_bun_button(driver)
        assert locators.wait_for_bun_text(driver) == 'Булки'

    def test_sauces_section(self, driver):
        locators.click_sign_in_to_account(driver)
        locators.login_with_default_data(driver)
        locators.click_to_constructor_button(driver)
        locators.click_to_sauces_link(driver)
        assert locators.wait_for_sauces_text(driver) == 'Соусы'

    def test_fillings_section(self, driver):
        locators.click_sign_in_to_account(driver)
        locators.login_with_default_data(driver)
        locators.click_to_constructor_button(driver)
        locators.click_to_fillings_link(driver)
        assert locators.wait_for_fillings_text(driver) == 'Начинки'


