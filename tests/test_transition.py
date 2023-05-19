from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransitions:
    def test_transition_to_lk(self, driver, default_email, default_password):
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
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_transition_from_lk_to_constructor(self, driver, default_email, default_password):
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
        # клик по кнопке "Конструктор"
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == "Соберите бургер"

    def test_transition_to_constructor_and_burgers_logo(self, driver, default_email, default_password):
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
        # клик по логотипу
        driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == 'Соберите бургер'
