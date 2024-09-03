from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('que eu me logo no site da "Luma Store"')
def step_impl(context):
    # Acessa a página inicial e realiza o login
    context.driver.get("https://magento.softwaretestingboard.com/")

    # Clica no botão "Sign In"
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'body > div.page-wrapper > header > div.panel.wrapper > div > ul > li.authorization-link > a'))
    ).click()

    # Insere o e-mail e a senha e faz login
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@name,"login[username]")]'))
    ).send_keys('bryan.benicio.moura@hushmail.com')

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@name,"login[password]")]'))
    ).send_keys('Senha#123456')

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#send2'))
    ).click()


@when('adiciono um produto aleatório do catalogo de moda masculina no carrinho')
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
        EC.element_to_be_clickable((By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[5]/div/a/span/span/img'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="option-label-size-143-item-170"]'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"swatch-option color")]'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"][contains(., "Add to Cart")]'))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(., "shopping cart")]'))
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
    screenshot_path = 'C:\\Users\\EddieSilva\\Desenvolvimentos\\Testes\\Challenge_Luma_Store\\features\\screenshot\\test_add_produto_aleatorio.png'
    context.driver.save_screenshot(screenshot_path)
    print(f'Screenshot salva em {screenshot_path}')
