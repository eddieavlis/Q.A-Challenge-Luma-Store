# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Adicionar um produto no carrinho

@test_5add_produto_carrinho
Cenario: Adicionar um produto no carrinho
  Dado que eu esteja na pagina da "Luma Store"
  Quando eu adicionar um produto no carrinho
  Entao um produto deve ser adicionado ao carrinho
