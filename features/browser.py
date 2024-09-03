from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    # Usa o ChromeDriverManager para gerenciar o chromedriver
    chrome_service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.maximize_window()  # Maximiza a tela
    return driver
