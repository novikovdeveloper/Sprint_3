from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# Клик по кнопке ЛК
def click_to_lk_button(driver):
    driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()


# Клик по кнопке "Войти в аккаунт"
def click_sign_in_to_account(driver):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()


# Клик по кнопке "Войти"
def click_to_login_button(driver):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()


def click_to_login_link(driver):
    driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()


# Клик по кнопке "Зарегистрироваться"
def click_registration_link(driver):
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()


def click_to_registration_button(driver):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()


# Задаем ожидание для кнопки "Вход" после успешной регистрации
def wait_for_login_text(driver):
    return WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]"))).text


# Ввод дефолтного имени
def set_name(driver):
    driver.find_element(By.XPATH, "//label[text()='Имя']/following::input[@type='text']").send_keys('Вася')


# Ввод дефолтного логина
def set_default_login(driver):
    driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys("test@1993.ru")


# Ввод дефолтного пароля
def set_default_password(driver):
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456")


# Ввод случайного email
def set_random_login(driver, random_email):
    driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@type='text']").send_keys(random_email)


# Ввод случайного пароля
def set_random_password(driver, random_password):
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(random_password)


# некорректный пароль
def set_incorrect_password(driver):
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("12345")


# ожидание сообщения об ошибке с неверным паролем
def wait_for_incorrect_password_text(driver):
    return driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]").text


# логинимся под дефолтными данными
def login_with_default_data(driver):
    set_default_login(driver)
    set_default_password(driver)
    click_to_login_button(driver)


# Ожидание сообщения "соберите бургер"
def wait_for_burger_page_text(driver):
    return WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))).text


# Клик по кнопке "Зарегистрироваться"
def click_to_register_button(driver):
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()


# Клик по кнопке "Восстановить пароль"
def click_to_reset_password_button(driver):
    driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()


def wait_for_account_profile_page_text(driver):
    return WebDriverWait(driver, 3).until(ec.url_contains("https://stellarburgers.nomoreparties.site/account/profile"))


# Клик по кнопке "Конструктор"
def click_to_constructor_button(driver):
    driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()


# Клик по кнопке "выход"
def click_to_logout_button(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()


# Клик по лого "Stellar burgers"
def click_to_burgers_logo(driver):
    driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()


# Клик по кнопке "Соусы"
def click_to_sauces_link(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()


# Клик по кнопке "Начинки"
def click_to_fillings_link(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()


# Клик по кнопке "Булки"
def click_to_bun_button(driver):
    driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]").click()


def wait_for_bun_text(driver):
    return driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text


def wait_for_sauces_text(driver):
    return driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text


def wait_for_fillings_text(driver):
    return driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").text


