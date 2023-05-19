
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_successful_registration(self, driver, name, random_email, random_password):
        # клик по ЛК
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        # клик по "Вы — новый пользователь? Зарегистрироваться"
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        # Ввод имени
        driver.find_element(By.XPATH, "//label[text()='Имя']/following::input[@type='text']").send_keys(name)
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(random_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(random_password)
        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//*[@id='root']/div/main/div/form/button").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Вход')]").text == "Вход"

    def test_incorrect_password_error(self, driver, name, default_email):
        # клик по ЛК
        driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()
        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        # Ввод имении
        driver.find_element(By.XPATH, "//label[text()='Имя']/following::input[@type='text']").send_keys(name)
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод некорректного пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123")
        # Клик по кнопке Зарегистрироваться
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        # Проверка, что появилось сообщение об ошибке
        assert driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'

