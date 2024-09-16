# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Realizar checkout de produto

@test_7checkout
Cenario: Realizar checkout
  Dado que eu me logo no site da "Luma Store"
  Quando eu adiciono produto ao carrinho
  E eu iniciao o processo de checkout
  Entao eu devo conseguir finalizar o checkout com sucesso
