# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar um produto aleatório

  @test_add_produto_aleatorio
Cenário: Adicionar um produto aleatório do catalogo de moda masculina no carrinho
  Dado que eu me logo no site da "Luma Store"
  Quando adiciono um produto aleatório do catalogo de moda masculina no carrinho
  Então devo visualizar o produto selecionado no carrinho
