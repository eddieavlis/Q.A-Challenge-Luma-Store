# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar comentario em um produto no carrinho

  @test_3add_comentario_em_produto
Cenário: Adicionar comentário em um produto aleatório do catálogo de moda masculina no carrinho
  Dado que eu acesso o site da "Luma Store"
  Quando eu adiciono um produto aleatório do catálogo de moda masculina ao carrinho
  E tento adicionar um comentário ao produto no carrinho
  Então devo verificar que não foi possível adicionar o comentário
