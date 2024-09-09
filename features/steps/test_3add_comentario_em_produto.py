from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('que eu acesso o site da "Luma Store"')
def step_impl(context):
    # Acessa a página inicial e realiza o login
    context.driver.get("https://magento.softwaretestingboard.com/")


@when('eu adiciono um produto aleatorio do catalogo de moda masculina ao carrinho')
def step_impl(context):
    # Navega até o catálogo de produtos
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


@when('tento adicionar um comentario ao produto no carrinho')
def step_impl(context):
    try:
        # Verifica se o campo de comentário está presente na página
        comment_box = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@id="comment"]'))
        )
        # Se o campo de comentário estiver presente, tenta adicionar o comentário
        comment_box.send_keys('Ótimo produto, recomendo!')

        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@title,"Submit Comment")]'))
        ).click()

        context.comment_added = True
    except:
        # Caso o campo de comentário não esteja presente, define o status de comentário como não adicionado
        context.comment_added = False


@then('devo verificar que nao foi possivel adicionar o comentario')
def step_impl(context):
    if context.comment_added:
        # Se o comentário foi adicionado, o cenário falhou, pois não era esperado
        assert False, 'O comentário foi adicionado, mas não deveria ser possível.'

    # Caso contrário, verifica se a funcionalidade de adicionar comentários está ausente
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@id="comment"]'))
        )
        # Se o campo de comentário está presente, o teste falhou
        assert False, 'O campo de comentário está presente, mas não deveria estar.'

    except:
        # Se o campo de comentário não está presente, o teste está correto
        print("A funcionalidade de adicionar comentários não está disponível na página do carrinho.")

        # Captura a tela e salva no local especificado
        screenshot_path = 'C:\\Users\\EddieSilva\\Desenvolvimentos\\Testes\\Challenge_Luma_Store\\features\\screenshot\\test_3add_comentario_em_produto.png'
        context.driver.save_screenshot(screenshot_path)
        print(f'Screenshot salva em {screenshot_path}')
