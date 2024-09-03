from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
import os


@given('que eu esteja na página da "Luma Store"')
def step_impl(context):
    try:
        # URL "Luma Store"
        product_url = "https://magento.softwaretestingboard.com/"
        context.driver.get(product_url)
    except NoSuchWindowException:
        print("A janela do navegador foi fechada. Verifique se o navegador está aberto.")
        raise


@when('eu adicionar um produto no carrinho')
def step_impl(context):
    try:
        # Adicionando produto no carrinho
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > div.columns > div > div.widget.block.block-static-block > div.block.widget.block-products-list.grid > div > div > ol > li:nth-child(4) > div > a > span > span > img"))
        ).click()

        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#option-label-size-143-item-170"))
        ).click()

        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#option-label-color-93-item-49"))
        ).click()

        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-addtocart-button"))
        ).click()

    except NoSuchWindowException:
        print("A janela do navegador foi fechada. Verifique se o navegador está aberto.")
        raise


@then('um produto deve ser adicionado ao carrinho')
def step_impl(context):
    try:
        # Acessa o carrinho para verificar os itens
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'shopping cart')]"))
        ).click()

        # Caminho para salvar a captura de tela
        screenshot_path = r'C:\Users\EddieSilva\Desenvolvimentos\Testes\Challenge_Luma_Store\features\screenshot\test_add_produto_carrinho.png'

        # Verificar se o diretório existe, e se não, criar
        screenshot_dir = os.path.dirname(screenshot_path)
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # Captura de tela com um produto no carrinho
        context.driver.save_screenshot(screenshot_path)

        # Validar que o produto consta no carrinho
        assert "Hero Hoodie" in context.driver.page_source

    except NoSuchWindowException:
        print("A janela do navegador foi fechada. Verifique se o navegador está aberto.")
        raise
