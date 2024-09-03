# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Realizar checkout de produto

  @test_checkout
Cenário: Realizar checkout
  Dado que eu me logo no site da "Luma Store"
  Quando adiciono produto ao carrinho
  E devo iniciar o processo de checkout
  Então eu devo conseguir finalizar o checkout com sucesso
