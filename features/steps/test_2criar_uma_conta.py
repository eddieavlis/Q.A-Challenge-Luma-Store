from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@given('que eu esteja na tela de Login/Cadastro')
def step_impl(context):
    context.driver.get("https://magento.softwaretestingboard.com/")

    # Clica no botão "Create an Account"
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.page-wrapper > header > div.panel.wrapper > div > ul > li:nth-child(3) > a'))
    ).click()


@when('eu preencher o formulario de criacao de conta com dados validos')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Preencher campos do formulário
    first_name_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[1]/div/input")))
    first_name_element.send_keys("Bira")
    last_name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'lastname')]")))
    last_name_element.send_keys("Silva Player Special")
    email_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email'][contains(@id,'address')]")))
    email_element.send_keys("bira.silva@special.com")
    password_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@title='Password']")))
    password_element.send_keys("Senha#123456")
    confirm_password_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'password_confirmation')]")))
    confirm_password_element.send_keys("Senha#123456")


@when('eu submeter o formulario')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    create_account_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-validate > div > div.primary > button")))
    create_account_button.click()


@then('uma nova conta deve ser criada com sucesso')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # Verifica se a conta foi criada com sucesso
    my_account_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='base'][contains(.,'My Account')]")))
    assert my_account_element.is_displayed()

    # Captura de tela após criar a conta
    screenshot_path = r"C:\Users\EddieSilva\Desenvolvimentos\Testes\Challenge_Luma_Store\features\screenshot\test_2criar_uma_conta.png"
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    context.driver.get_screenshot_as_file(screenshot_path)
    print(f"Captura de tela salva em: {screenshot_path}")

    # Processo de Sign Out
    try:
        # Clique no nome do usuário para abrir o menu
        account_menu_element = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.customer-welcome > span'))
        )
        account_menu_element.click()

        # Clique no link de Sign Out
        sign_out_element = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.customer-welcome.active > div > ul > li.authorization-link > a'))
        )
        sign_out_element.click()
        print("Usuário deslogado com sucesso.")

    except Exception as e:
        print(f"Erro durante o processo de Sign Out: {e}")
        # Captura de tela em caso de erro
        screenshot_path_fail = r"C:\Users\EddieSilva\Desenvolvimentos\Testes\Challenge_Luma_Store\features\screenshot\test_2criar_uma_conta_fail.png"
        context.driver.get_screenshot_as_file(screenshot_path_fail)
        print(f"Captura de tela de falha salva em: {screenshot_path_fail}")
        assert False, f"Erro durante o processo de Sign Out: {e}"
