# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar um produto no carrinho

  @test_add_produto_carrinho
Cenário: Adicionar um produto no carrinho
  Dado que eu esteja na página da "Luma Store"
  Quando eu adicionar um produto no carrinho
  Então um produto deve ser adicionado ao carrinho
