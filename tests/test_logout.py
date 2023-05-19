from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_logout_from_lk(self, driver, default_password, default_email):
        # клик по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        # клик по кнопке "Личный Кабинет"
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains("https://stellarburgers.nomoreparties.site/account/profile"))
        # клик по кнопке "Выход"
        driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'