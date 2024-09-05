# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Acessar a pagina da "Luma Store"

  @test_1acessar_home_page
Cenário: Se a página está carregando corretamente a home page da "Luma Store"
  Dado que eu acesso a página inicial da Luma Store
  Quando a página carregar
  Então a home page da "Luma Store" deve ser exibida corretamente
