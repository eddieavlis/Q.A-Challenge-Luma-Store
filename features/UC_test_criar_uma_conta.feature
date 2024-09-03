# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Criação de conta

  @test_criar_uma_conta
Cenário: Criar uma conta na tela de Login/Cadastro
  Dado que eu esteja na tela de Login/Cadastro
  Quando eu preencher o formulário de criação de conta com dados válidos
  E eu submeter o formulário
  Então uma nova conta deve ser criada com sucesso
