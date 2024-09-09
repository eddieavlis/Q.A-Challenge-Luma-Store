# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Acessar a pagina da "Luma Store"

@test_1acessar_home_page
Cenario: Se a pagina esta carregando corretamente a home page da "Luma Store"
  Dado que eu acesso a pagina inicial da Luma Store
  Quando a pagina carregar
  Entao a home page da "Luma Store" deve ser exibida corretamente
