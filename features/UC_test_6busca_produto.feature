# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Busca de produto

A pagina carrega com produtos e especificacoes diferente da esperada | vide imagem: test_6busca_produto.png"

@test_6busca_produto
Cenario: Buscar por "shirt" clicar no ultimo resultado sugerido no campo de busca no menu superior e revisar se a pagina de resultados carregou corretamente
  Dado que eu estou na pagina inicial da "Luma Store"
  Quando eu busco por "shirt" clico no ultimo resultado sugerido usando o campo de busca no menu superior
  Entao eu devo visualizar a pagina Search results for: "ultimo resultado sugerido"
