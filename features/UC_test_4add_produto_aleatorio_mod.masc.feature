# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar um produto aleatorio

  @test_4add_produto_aleatorio_mod.masc
Cenário: Adicionar um produto aleatório do catalogo de moda masculina no carrinho
  Dado que acesso o site da "Luma Store"
  Quando adiciono um produto aleatório do catalogo de moda masculina no carrinho
  Então devo visualizar o produto selecionado no carrinho
