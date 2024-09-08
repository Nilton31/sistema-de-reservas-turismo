# Trabalho de Extensão Acadêmico

## Projeto de Sistema de reservas para Pontos de Turismo

### Cenario
Foi identificada a necessidade de substituir os registros manuais por um sistema que faça a integração com banco de dados relacional 
visando um melhor desempenho e agilidade principalmente na localização dos registros dos clientes junto com a descrição dos destinos 
para elaboração de perfis dos seus usuários.

### Demanda sociocomunitário e motivação acadêmica 
Aplicação dos meus conhecimentos sobre a linguagem de programação python e a bioblioteca SQLITE3 contemplará a empresa 
com um monitoramento das reservas e adição de novos clientes ao sistema visando um atendimento ainda mais ágil.

### Objetivos a serem alcançados em relação à situação-problema identificada

#### 1. Identifica os requisitos:
Identifica os requisitos funcionais e decompor o problema principal para uma melhor eficaz na resolução de problemas.

#### 2. Desenvolvimento do Sistema:
Desenvolver um sistema com python para integração com banco de dados relacional utilizando a biblioteca sqlite3.

#### 3. Comunicação:
Ao inicial o projeto e no seu final é importante estabelecer uma comunicação simples e direta entre membros da equipe para 
maiores entendimentos.

### Plano de Trabalho com Cronograma das Atividades
#### Objetivo: 
Desenvolver um sistema em python em modo texto que alimente um banco de dados com os dados pessoais dos seus clientes/usuários utilizando a biblioteca sqlite3.

##### Ação 1: 
Realizar planejamento de como será feito o desenvolvimento até o dia ( 10/06 ).

##### Ação 2:
Ler os conteúdos nas referencias Introdução à Programação com Python Algoritmos e Lógica de Programação para Iniciantes e SQLITEBROWSER. DB BROWSER FOR SQLITE.

##### Ação 3: 
Elaborando um fluxograma para esquematiza o sistema e um modelo conceitual lógico DER até o dia ( 11/06 ).

##### Ação 4: 
Reunião com os membros da empresa para defini os requisitos funcionais até o dia (12/06) de forma remota em na cidade de 
Fortaleza Ceará.

##### Ação 5: 
Criação dos scripts em python das funções para criação do banco e definição das tabelas até ( 15/06 ) em home office - Fortaleza. 

##### Ação 6: 
Inserção de dados teste no banco até o dia ( 18/06 ) em home office - Fortaleza.

##### Ação 7: 
Modificações técnicas nas funções da Tabelas e organização até o dia ( 21/06 ) em home office - Fortaleza.

##### Ação 8: 
Adiciona as tabelas usuários, destinos, reservas até o dia ( 25/06 ) em home office - Fortaleza.

##### Ação 9: 
Revisão e entrega do projeto a empresa até o dia ( 04/08 ).

### Minhas Responsabilidades

##### 1. Análise de Requisitos: 
identificar e documenta os requisitos do banco de dados e sistema.

##### 2. Modelagem de Dados: 
criar modelos conceitos, lógicos e físicos para o banco de dados.

##### 3. Implementação:  
desenvolver e implementar o banco de dados incluído a criação tabelas e índices.

##### 4.Criação do Fluxograma Lógico: 
criar entidades que representam as funcionalidades do sistema e usuários.
link https://drive.google.com/file/d/1ZqT0sbquvx9C8guLtfG7uDV_j2ccSzSa/view?usp=sharing

##### 5. Teste do sistema e avalição:  
elaborei testes com dados ilustrativos para fim checa o desempenho do sistema.

### Detalhamento do Fluxograma

![16062_192736_fluxograma-sistema1](https://github.com/user-attachments/assets/35c65a7a-4f02-4a3c-9540-8307d1f36425)

 ### Introdução
 No fluxograma é demostrado o funcionamento do sistema responsável por alimenta o  banco de dados ( viagens ) 7.
 Componentes
##### elipses: 
representam o inicio e fim do sistema respectivamente conforme é mostrado 1 e 28.
##### retângulos: 
são representações das funções do sistema.
##### losangos: 
é a representação da estrutura match case do python ela é equivalente a swich case de outras linguagens de programação a sua principal 
funcionalidade é tomar decisão de acordo com alguma ação que o nosso usuário escolhe.

### Tipos de Ligações (setas)

<ul>
<li>setas verdes são conexões entre funções.</li>
<li>setas amarelo e a estrutura match case de decisão.</li>
<li>setas vermelhas são interações de retorno de funções anteriores.</li>
<li>setas azuis são conexões com banco de dados.</li>
</ul>

### Passo a passo

#### Inicio do Sistema:

Como foi dito anteriormente a primeira elipsa traz a representação do inicio do sistema, ou seja, 
o nosso usuário no caso o atendente que realiza a manipulações dos clientes / usuários que vão entra 
em contato via telefonema.

#### Acessa Sistema:

No primeiro retângulo temos a primeira função chamada Acessar_Sistema() a sua utilidade é apresenta uma mensagem de "BEM VINDO AO PORTAL DE VIAGENS", 
e em seguida é exibindo 10 opções cada iria desempenha uma função específica.

#### Verificar Botão:

Essa função cuidara de complementa a função anteiro ela receberá a opção que o nosso atendente digitara logo depois a mesma realizara uma 
verificação de qual opção foi escolhida e chamara a sua função específica equivalente.

<ul>
  <li>opção 1: já no primeiro losango temos a primeira opção de número 1 e ser foi selecionada chamara a função de 5 Colata_Dados_Usuarios(), que 
    solicitara o atendente os dados pessoais do cliente/usuário depois o sistema passara essas informações a função 6 Tabela_Usuario() em seguida 
    salvara as alterações no banco de viagens 7.Também na opção vamos ter o menu, que retornara todas as opções em todas as opções.</li>
  <li>opção 2: nessa opção o sistema fara uma consulta de todos os usuários cadastrados no banco a função 16 Consulta_Usuario() cuidara disso.</li>
  <li>opção 3: aqui foi definida 12 Atualizar_Dados_Usuarios() será responsável para atualizar os dados de endereço esses dados vão ser 
    tratados mais adiante com atualização salvas no banco passamos agora  para o próxima opção.</li>
  <li>opção 4: na opção 4 temos a função  14 Excluir_Cadastro_Usuarios(), que receberá o cpf do usuário para localiza o cadastro no banco para apagar. 
    Perceba que temos uma seta vermelha retornando para o losango da opção 2 isso ser da pelo o campo exibido após a execução da função exclui objetivo
    disso é virsualiza a lista de usuários afim de mostra o sucesso da operação em seguida conecta ao banco como é mostrado na seta azul.</li>
  <li>opção 5:  assim como a função consulta_usuarios() na opção 2 vamos ter 16 Consulta_Destinos(), mais aqui invés de consulta usuários ela 
     consultara os destinos cadastrados no banco a função chamara o 10 menu() logo depois de mostra os destinos.</li>
  <li>opção 6: aqui ser desejamos adicionar novos destinos para os usuários 18 Coleta_Dados_Destinos(), que exibira quais dados serão perdidos para 
     cadastra no banco na 19 Tabela_Destinos() receberão esses paramentos  e em seguida envia-la ao banco e como foi dito essa funcionalidade itera 
     para chama a função Menu().</li>
  <li>opção 7: a função  21 Excluir_Cadastro_Destino(), que recebera como paramento o nome do destino para excluir do banco essa funcionalidade retornara 
      a ação da opção 5 para visualiza se o destino foi deletado dos registro do banco como é mostrado pela seta vermelha.</li>
  <li>opção 8: 23 Realizar_Reservas() fornecera as orientações para realiza uma reserva essa informações serão passadas a 24 Tabela_Reservas.(), que 
    chamara Menu() e longo em seguida salva no banco.</li>
  <li>opção 9: 26 Visualizar_Reservas() estabelecera uma conexão com o banco e exibira as reservas finalizado a chamada Menu().</li>
  <li>opção 10: por fim temos a opção 10 que representara a saída do sistema.</li>

 ### Diagrama Entidade e Relacionamento
No diagrama entidade e relacionamento (DER) é mostrado três entidades usuários , reservas, destinos e seus relacionamentos realiza e vincula esses 
diagramas demostra uma visão interna do banco de dados viagens do fluxograma anterior.

Na entidade usuários temos os atributos id (chave primaria) nome, data de nascimento, rua endereço, endereço de e-mail, numero da residencia, 
cidade estado e país conforme é mostrado um usuário pode ter uma ou varias reservas e já as reservas no mínimo um usuários ou vários 
destinos vinculados.

![der](https://github.com/user-attachments/assets/bfeabe3e-334a-4b8a-ad7d-bb8d06a8c57e)

</ul>
