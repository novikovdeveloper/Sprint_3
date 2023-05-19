from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSignIn:
    def test_sign_in_on_main_page(self, driver, default_email, default_password):
        # клик по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == "Соберите бургер"

    def test_sign_in_by_lk_button(self, driver, default_email, default_password):
        # клик по кнопке "Личный кабинет"
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == "Соберите бургер"

    def test_sign_in_by_registration_form(self, driver, default_email, default_password):
        # клик по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # клик по "Вы — новый пользователь? Зарегистрироваться"
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        # клик по "Войти"
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == "Соберите бургер"

    def test_sign_in_by_reset_password_form(self, driver, default_email, default_password):
        # клик по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # клик по "Восстановить пароль"
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        # клик по "Войти"
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == "Соберите бургер"