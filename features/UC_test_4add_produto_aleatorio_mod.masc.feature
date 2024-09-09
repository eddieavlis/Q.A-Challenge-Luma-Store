# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar um produto aleatorio

@test_4add_produto_aleatorio_mod.masc
Cenario: Adicionar um produto aleatorio do catalogo de moda masculina no carrinho
  Dado que acesso o site da "Luma Store"
  Quando adiciono um produto aleatorio do catalogo de moda masculina no carrinho
  Entao devo visualizar o produto selecionado no carrinho
