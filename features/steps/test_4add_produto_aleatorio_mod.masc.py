from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('que acesso o site da "Luma Store"')
def step_impl(context):
    # Acessa a página inicial e realiza o login
    context.driver.get("https://magento.softwaretestingboard.com/")


@when('adiciono um produto aleatorio do catalogo de moda masculina no carrinho')
def step_impl(context):
    # Navega até o catálogo de moda masculina
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ui-id-5'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#narrow-by-list2 > dd > ol > li:nth-child(1) > a'))
    ).click()

    # Adiciona o produto ao carrinho
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

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#maincontent > div.page.messages > div:nth-child(2) > div > div > div > a'))
    ).click()


@then('devo visualizar o produto selecionado no carrinho')
def step_impl(context):
    # Valida que o produto foi adicionado ao carrinho
    product_name = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#shopping-cart-table > tbody > tr.item-info > td.col.item > div > strong > a'))
    )
    assert product_name.is_displayed(), 'Produto não encontrado no carrinho'

    # Captura a tela e salva na pasta especificada
    screenshot_path = 'C:\\Users\\EddieSilva\\Desenvolvimentos\\Testes\\Challenge_Luma_Store\\features\\screenshot\\test_4add_produto_aleatorio_mod.masc.png'
    context.driver.save_screenshot(screenshot_path)
    print(f'Screenshot salva em {screenshot_path}')
