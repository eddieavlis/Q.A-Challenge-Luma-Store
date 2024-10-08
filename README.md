# Q.A Challenge Luma Store

Este projeto é uma solução de testes automatizados para o site Luma Store, desenvolvido como parte do desafio proposto pela Coodesh. O objetivo é garantir a qualidade e a funcionalidade do site através de testes estruturados e automatizados, aplicando conceitos de teste caixa preta e uma abordagem baseada em BDD (Behavior-Driven Development).

## Tecnologias e Ferramentas Utilizadas

- **Python**: Linguagem principal para a implementação dos testes automatizados, proporcionando flexibilidade e eficiência na execução dos scripts.
- **Selenium**: Ferramenta essencial para a automação da interação com o navegador, permitindo a simulação de ações do usuário e a validação do comportamento do site.
- **Behave**: Biblioteca para BDD em Python, usada para definir e executar os testes de forma legível e alinhada aos requisitos do projeto.
- **Gherkin**: Linguagem para escrever os casos de uso em um formato compreensível para desenvolvedores e stakeholders, facilitando a colaboração e a clareza dos testes.

## Abordagem

O projeto segue a metodologia BDD, onde os casos de uso são descritos em um formato de especificação de comportamento usando Gherkin. Isso permite uma comunicação eficaz entre as partes interessadas e assegura que os testes reflitam com precisão os requisitos do negócio. Os casos de uso são implementados e executados utilizando Behave em conjunto com o Selenium para validar a funcionalidade do Luma Store de maneira automatizada.

## Processo de Pensamento e Decisões

### Definição da Abordagem e Escopo

Baseado nos Casos de Uso propostos pelo desafio da Coodesh, os cenários foram escritos em Gherkin para cobrir aspectos essenciais do site, como navegação, busca de produtos, adição ao carrinho e finalização da compra.

### Escolha das Ferramentas e Tecnologias

**Vantagens das Ferramentas Escolhidas:**

- **Python e Selenium**: Python foi escolhido pela sua versatilidade e sintaxe simples. Selenium foi escolhido pela sua robustez na automação de navegadores e na simulação de interações do usuário.
- **Behave e Gherkin**: Behave foi utilizado para implementar BDD e Gherkin para escrever casos de uso de forma compreensível e colaborativa, facilitando a tradução dos requisitos de negócio em testes executáveis.

**Desvantagens das Ferramentas Não Escolhidas:**

- **Cypress**: Configuração para testes paralelos complicada e suporte limitado para outros navegadores.
- **Ghost Inspector**: Menos flexível e customizável em comparação com outras ferramentas.
- **Robot Framework**: Integração mais complexa.

## Desenvolvimento e Execução dos Testes

1. **Escrita dos Cenários em Gherkin**: Cenários descritos em uma linguagem natural e acessível.
2. **Implementação com Behave e Selenium**: Cenários implementados utilizando Behave para integração com o Selenium.
3. **Execução e Validação**: Testes executados com sucesso na maioria dos casos. Um desafio encontrado foi no teste de "Realizar checkout", onde os botões "Next" e "Place Order" não estavam clicando devido ao erro "ElementClickInterceptedException". Foi utilizada uma abordagem com JavaScript para forçar o clique e concluir o teste.

## Instalação e Uso do Projeto

### Instalações Necessárias

1. **Python**:
   - Versões compatíveis: 3.10, 3.11, 3.12
   - Download: [Python Downloads](https://www.python.org/downloads/)

2. **Selenium**:
   - Instalação via terminal: `pip install selenium`

3. **Behave**:
   - Instalação via terminal: `pip install behave`

4. **IDE Utilizada**: PyCharm
   - Plugin Gherkin para suporte ao desenvolvimento.

### Executar os Testes

Executar e gerar o relatório de teste do Challenge Luma Store.
Na pasta raiz do projeto, digite. behave --format html --outfile reports/test-report.html

Executar os testes por caso de uso individualmente.
Na pasta raiz do projeto, digite. behave features/nome_do_caso_de_uso.feature

**Exemplos**:

\Challenge_Luma_Store> behave --format html --outfile reports/test-report.html

\Challenge_Luma_Store>behave features/UC_test_1acessar_home_page.feature

Siga estas instruções para configurar o ambiente e iniciar a execução dos testes automatizados para o Luma Store.

---

Para mais detalhes, sinta-se à vontade para explorar o código e os cenários de teste incluídos neste repositório.
