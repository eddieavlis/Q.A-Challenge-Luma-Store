from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
import os


@given('que eu estou na pagina inicial da "Luma Store"')
def step_impl(context):
    context.driver.get("https://magento.softwaretestingboard.com/")
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Home Page")
    )


@when('eu busco por "shirt" usando o campo de busca no menu superior')
def step_impl(context):
    search_box = context.driver.find_element(By.CSS_SELECTOR, "#search")
    search_box.send_keys("shirt")

    # Espera até que a lista de sugestões apareça
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#search"))
    )

    # Espera até que o último item da lista seja visível e clicável
    last_suggestion = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#qs-option-7"))
    )
    last_suggestion.click()


@then('eu devo visualizar a pagina Search results for: "ultimo resultado sugerido"')
def step_impl(context):
    # Aplica o zoom de 50% na página
    context.driver.execute_script("document.body.style.zoom='50%'")

    # Caminho para salvar a captura de tela
    screenshot_path = r"C:\Users\EddieSilva\Desenvolvimentos\Testes\Challenge_Luma_Store\features\screenshot\test_6busca_produto.png"

    try:
        # Verifica se a página de resultados carregou
        print("Aguardando titulo da pagina...")
        WebDriverWait(context.driver, 10).until(
            EC.title_contains("Search results for:")
        )
        print("Titulo da pagina encontrado.")

        # Verifica se um item não esperado está presente na página
        unwanted_item_xpath = "//a[@class='product-item-link'][contains(.,'Radiant Tee')]"
        unwanted_items = context.driver.find_elements(By.XPATH, unwanted_item_xpath)

        if unwanted_items:
            # Se o item não esperado estiver presente, falhe o teste
            print(f"Item nao esperado 'Radiant Tee' encontrado na pagina de resultados.")
            # Captura de tela para evidência
            context.driver.save_screenshot(screenshot_path)
            print(f"Captura de tela salva em {screenshot_path}")
            assert False, "Item nao esperado 'Radiant Tee' encontrado na pagina de resultados."

        print("Nenhum item não esperado encontrado.")

    except TimeoutException as e:
        print(f"Erro de Timeout: {e}")
        # Captura de tela em caso de timeout
        context.driver.save_screenshot(screenshot_path)
        print(f"Captura de tela salva em {screenshot_path}")
        assert False, f"Timeout ao esperar pelo título da página: {e}"

    except Exception as e:
        print(f"Erro inesperado: {e}")
        # Captura de tela em caso de erro inesperado
        context.driver.save_screenshot(screenshot_path)
        print(f"Captura de tela salva em {screenshot_path}")
        assert False, f"Erro inesperado: {e}"
