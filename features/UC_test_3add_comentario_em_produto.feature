# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar comentario em um produto no carrinho

@test_3add_comentario_em_produto
Cenario: Adicionar comentario em um produto aleatorio do catalogo de moda masculina no carrinho
  Dado que eu acesso o site da "Luma Store"
  Quando eu adiciono um produto aleatorio do catalogo de moda masculina ao carrinho
  E tento adicionar um comentario ao produto no carrinho
  Entao devo verificar que nao foi possivel adicionar o comentario
