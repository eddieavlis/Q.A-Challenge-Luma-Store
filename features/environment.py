from features.browser import get_driver
import os


def before_all(context):
    """
    Executado uma vez antes de todos os cenários.
    Configura o navegador e o contexto global do teste.
    """
    context.driver = get_driver()


def after_all(context):
    """
    Executado uma vez após todos os cenários.
    Encerra o navegador.
    """
    context.driver.quit()
