# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Busca de produto

  @test_busca_produto
Cenário: Buscar por "shirt" e clicar no último resultado sugerido e revisar se a página de resultados carregou corretamente
  Dado que eu estou na página inicial da "Luma Store"
  Quando eu busco por "shirt" usando o campo de busca no menu superior
  Então eu devo clicar no último resultado sugerido
  E eu devo visualizar as informações do produto selecionado
