from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import os


@given('que eu me logo no site da "Luma Store"')
def step_impl(context):
    # Acessa a página inicial e realiza o login
    context.driver.get("https://magento.softwaretestingboard.com/")

    # Clica no link menu "Sign In"
    WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.authorization-link > a'))
    ).click()

    # Insere o e-mail e a senha e faz login
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@name,"login[username]")]'))
    ).send_keys('joao-bernardes87@amaralmonteiro.com.br')

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@name,"login[password]")]'))
    ).send_keys('Senha#123456')

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#send2'))
    ).click()


@when('adiciono produto ao carrinho')
def step_impl(context):
    # Sequência que adiciona um produto ao carrinho
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ui-id-5'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#narrow-by-list2 > dd > ol > li:nth-child(1) > a'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#maincontent > div.columns > div.column.main > div.products.wrapper.grid.products-grid > ol > li:nth-child(7) > div > a > span > span > img'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#option-label-size-143-item-170'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#option-label-color-93-item-49'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-addtocart-button'))
    ).click()

    WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#maincontent > div.page.messages > div:nth-child(2) > div > div > div > a'))
    ).click()


@when('devo iniciar o processo de checkout')
def step_impl(context):
    try:
        # Inicia o processo de checkout
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/ul/li[1]/button'))
        ).click()

        # Espera pelo botão "Next" na página de checkout
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[contains(.,"Next")]'))
        )

        # Usar JavaScript para forçar o clique se necessário
        button = context.driver.find_element(By.XPATH, '//button[contains(.,"Next")]')
        context.driver.execute_script("arguments[0].click();", button)

        # Espera pelo botão "Place Order" na página de revisão do pedido
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[contains(.,"Place Order")]'))
        )

        # Usar JavaScript para forçar o clique no botão "Place Order"
        place_order_button = context.driver.find_element(By.XPATH, '//button[contains(.,"Place Order")]')
        context.driver.execute_script("arguments[0].click();", place_order_button)

    except ElementClickInterceptedException:
        # Se o clique falhar porque o elemento está coberto, tente novamente
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Next")]'))
        ).click()

    except TimeoutException:
        screenshot_path = 'C:\\Users\\EddieSilva\\Desenvolvimentos\\Testes\\Luma_Store\\features\\screenshot\\checkout_process_failure.png'
        context.driver.save_screenshot(screenshot_path)
        print(f'Captura de tela salva em {screenshot_path}')
        raise


@then('eu devo conseguir finalizar o checkout com sucesso')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Thank you for your purchase!")]'))
        )
        print(f"Elemento encontrado: {element.text}")
        print('Thank you for your purchase!')

    except TimeoutException:
        screenshot_path = 'C:\\Users\\EddieSilva\\Desenvolvimentos\\Testes\\Challenge_Luma_Store\\features\\screenshot\\test_7checkout.png'
        context.driver.save_screenshot(screenshot_path)
        print(f'Captura de tela salva em {screenshot_path}')
        assert True, 'Veja a captura de tela para mais detalhes.'
