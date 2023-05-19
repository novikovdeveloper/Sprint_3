from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    def test_bun_section(self, driver, default_email, default_password):
        # клик по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        #Клик по кнопке "Конструктор"
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        #Клик по кнопке "Соусы", для срабатывания перехода к кнопке с булками
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        #Клик по кнопке "Булки"
        driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text == 'Булки'

    def test_sauces_section(self, driver, default_email, default_password):
        # клик по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        #Клик по кнопке "Конструктор"
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        # Клик по кнопке "Соусы"
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Соусы')]")))
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text == 'Соусы'

    def test_fillings_section(self, driver, default_email, default_password):
        # клик по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        # Ввод email
        driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(default_email)
        # Ввод пароля
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(default_password)
        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        #Клик по кнопке "Конструктор"
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        # Клик по кнопке "Начинки"
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Начинки')]")))
        assert driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").text == 'Начинки'


