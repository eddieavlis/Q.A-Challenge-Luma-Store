import os
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.home_page import HomePage
from features.browser import get_driver
import pytest


@given('que eu acesso a página inicial da Luma Store')
def step_impl(context):
    # Instanciar a HomePage e abrir a página
    context.home_page = HomePage(context.driver)
    context.home_page.open()


@when('a página carregar')
def step_impl(context):
    # Espera até que a página inicial carregue corretamente
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Home Page")
    )


@then('a home page da "Luma Store" deve ser exibida corretamente')
def step_impl(context):
    # Verifica se a página inicial foi carregada corretamente
    screenshot_path = r"C:\Users\EddieSilva\Desenvolvimentos\Testes\Challenge_Luma_Store\features\screenshot\test_1acessar_home_page.png"

    # Cria o diretório para a captura de tela, se não existir
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

    # Captura a tela
    context.driver.get_screenshot_as_file(screenshot_path)

    # Imprime o caminho da captura de tela
    print(f"Captura de tela salva em: {screenshot_path}")

    # Verifica o título da página
    assert "Home Page" in context.driver.title
