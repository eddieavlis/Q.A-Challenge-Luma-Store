# language: pt

# Gherkin

# Casos de Uso:


Funcionalidade: Criar uma conta

@test_2criar_uma_conta
Cenario: Criar uma conta na tela de Login/Cadastro
  Dado que eu esteja na tela de Login/Cadastro
  Quando eu preencher o formulario de criacao de conta com dados validos
  E eu submeter o formulario
  Entao uma nova conta deve ser criada com sucesso
