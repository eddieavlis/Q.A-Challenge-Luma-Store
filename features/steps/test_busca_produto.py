from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
import os


@given('que eu estou na página inicial da "Luma Store"')
def step_impl(context):
    context.driver.get("https://magento.softwaretestingboard.com/")
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Home Page")
    )

@when('eu busco por "shirt" usando o campo de busca no menu superior')
def step_impl(context):
    search_box = context.driver.find_element(By.CSS_SELECTOR, "#search")
    search_box.send_keys("shirt")
    search_box.submit()

@then('eu devo clicar no último resultado sugerido')
def step_impl(context):
    # Espera as sugestões aparecerem
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#maincontent .products-grid"))
    )
    # Localiza o último resultado sugerido e clica
    last_product = context.driver.find_element(By.CSS_SELECTOR, "#maincontent > div.columns > div.column.main > div.search.results > div.products.wrapper.grid.products-grid > ol > li:nth-last-child(1) > div > a")
    last_product.click()

@then('eu devo visualizar as informações do produto selecionado')
def step_impl(context):
    try:
        # Espera o título da página mudar para o nome do produto
        WebDriverWait(context.driver, 10).until(
            EC.title_contains("Proteus Fitness Jackshirt")
        )
        # Assegura que o título da página contém o nome do produto
        assert "Proteus Fitness Jackshirt" in context.driver.title

        # Verifica se o título do produto na página é correto
        product_title_element = context.driver.find_element(By.CSS_SELECTOR, "#maincontent > div.columns > div > div.product-info-main > div.page-title-wrapper.product > h1")
        product_title = product_title_element.text
        assert product_title == "Proteus Fitness Jackshirt", f"Esperado: 'Proteus Fitness Jackshirt', Encontrado: '{product_title}'"

        # Define o diretório para capturas de tela e o caminho do arquivo
        screenshot_dir = r"C:\Users\EddieSilva\Desenvolvimentos\Testes\Challenge_Luma_Store\features\screenshot"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, "test_busca_produto.png")

        # Captura de tela da página do produto para validação
        context.driver.save_screenshot(screenshot_path)
        print(f"Captura de tela salva em: {screenshot_path}")

    except NoSuchWindowException:
        print("A janela do navegador foi fechada. Verifique se o navegador está aberto.")
        raise
