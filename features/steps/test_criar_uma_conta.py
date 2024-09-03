from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@given('que eu esteja na tela de Login/Cadastro')
def step_impl(context):
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

@when('eu preencher o formulário de criação de conta com dados válidos')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Preencher campos do formulário
    first_name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'firstname')]")))
    first_name_element.send_keys("Luan")
    last_name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'lastname')]")))
    last_name_element.send_keys("Lorenzo Ferreira")
    email_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email'][contains(@id,'address')]")))
    email_element.send_keys("luan_lorenzo_ferreira@focoreducao.com.br")
    password_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@title='Password']")))
    password_element.send_keys("Senha#654123")
    confirm_password_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password_confirmation')]")))
    confirm_password_element.send_keys("Senha#654123")

@when('eu submeter o formulário')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(.,'Create an Account')]")))
    create_account_button.click()

@then('uma nova conta deve ser criada com sucesso')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    my_account_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='base'][contains(.,'My Account')]")))
    assert my_account_element.is_displayed()
    screenshot_path = r"C:\Users\EddieSilva\Desenvolvimentos\Testes\Challenge_Luma_Store\features\screenshot\test_criar_uma_conta.png"
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    context.driver.get_screenshot_as_file(screenshot_path)
    print(f"Captura de tela salva em: {screenshot_path}")
