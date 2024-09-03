# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar comentário em um produto no carrinho

  @test_add_comentario_em_produto
Cenário: Adicionar comentário em um produto aleatório do catálogo de moda masculina no carrinho
  Dado que eu estou autenticado no site da "Luma Store"
  Quando eu adiciono um produto aleatório do catálogo de moda masculina ao carrinho
  E tento adicionar um comentário ao produto no carrinho
  Então devo verificar que não foi possível adicionar o comentário
