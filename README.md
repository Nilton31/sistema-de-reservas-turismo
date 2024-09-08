# Trabalho de Extensão Acadêmico

## Projeto de Sistema de reservas para Pontos de Turismo (Portal de Viagens)

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
  </ul>

 ### Diagrama Entidade e Relacionamento
No diagrama entidade e relacionamento (DER) é mostrado três entidades usuários , reservas, destinos e seus relacionamentos realiza e vincula esses 
diagramas demostra uma visão interna do banco de dados viagens do fluxograma anterior.

Na entidade usuários temos os atributos id (chave primaria) nome, data de nascimento, rua endereço, endereço de e-mail, numero da residencia, 
cidade estado e país conforme é mostrado um usuário pode ter uma ou varias reservas e já as reservas no mínimo um usuários ou vários 
destinos vinculados.

![der](https://github.com/user-attachments/assets/bfeabe3e-334a-4b8a-ad7d-bb8d06a8c57e)


#### Selecionando Banco de Dados
Nessa primeira imagem podemos ver o banco viagens sendo selecionado pelo o software DB BROWSER for SQLITE conforme é notado pela seta vermelha.

![16062_192736_selecionando_banco1](https://github.com/user-attachments/assets/a3ea3c37-b6df-4d9d-8c33-efbd1458d6da)

#### Visualizando as Tabelas
Na imagem abaixo podemos olha as 4 tabelas destinos, reservas e usuários todas definidas com seus esquema e principalmente com id (INTEGER PRIMARY KEY AUTOINCREMENT), ou seja, o id 
é a nossa chave primaria do tipo inteiro automática isso servira para identifica os registros no banco.

![16062_192736_mostrando_tabelas1](https://github.com/user-attachments/assets/4f6c7ccb-34b5-4f23-ac75-0e7161392d5d)

### Tabela Usuário
A tabela usuário mostra os 9 atributos id do tipo INTEGER (inteiro) nome do tipo text ( texto e seu tamanho de 255 ), cpf data_nascimento endereco_email 
também estão como interger já rua cidade numero e estado estão respectivamente com varchar de 255 text (150) e estado text(60).

![16062_192736_tabela_usuario1](https://github.com/user-attachments/assets/e6789222-f340-4e78-9d22-4e02557dda91)

#### Tabela Destinos
Na tabela destino temos os lugares de destino com suas identificações id o nome text(225) e sua descrição varcha(60).

![16062_192736_tabela_destinos1](https://github.com/user-attachments/assets/0d085e5b-ec89-48db-8447-d97acf8698c6)

#### Tabela Reservas
Finalmente temos a nossa ultima tabela que armazenara as reservas dos destinos escolhidos pelos os usuários para isso vamos tem os id(s) id_usuario e id_destino desempenham serviços de chaves estrangeiras que vão ser referencias nas busca dos registros das tabelas usuários e destinos. os status indicara ser a reserva está confirmada ou cancelada e para finaliza temos data que armazenara as datas de realização das reservas.

![16062_192736_tabela_reservas1](https://github.com/user-attachments/assets/03595196-f7ed-43eb-bcf2-8f27a4073205)

### Manual de Ultilização Portal de Viagens

A seguir será mostrado a ultilização do sistema:

#### Tela de Acesso ao Sistema
Nessa primeira tela está sendo exibido uma mensagem de "BEM VINDO AO PORTAL DE VIAGENS"  e o menu de 10 opções a opção de número 1 é a primeira que vamos trabalha no próximo tópico.

![16062_192736_tela_acesso1](https://github.com/user-attachments/assets/8daa8953-c356-4b2a-adda-7099d5f341b6)

#### Adicionando Usuário
Continuado com opção 1 a mesma nós fornecera instruções para cadastra um novo usuário no perceba que passamos o nome ( Isadora ) , cpf, data de nascimento nome da rua, cidade, a numeração da residência e estado todos os dados como exemplo no final recebemos que o nosso novo usuário foi cadastrado com sucesso.

![16062_192736_adicionando_usuario1](https://github.com/user-attachments/assets/7b909614-e1b2-4b67-b89d-27b09868bbd7)

#### Visualizado Usuário Cadastro
Ao digitar 2 podermos visualizar todos os usuários cadastro no banco perceba que o nosso usuário (Isadora) está localizado na ultima posição com id de número 20 conforme é mostrado. 

![16062_192736_visualizando_usuarios1](https://github.com/user-attachments/assets/23add0f1-356a-4da0-8675-0964a3b9275b)

#### Atualização endereço do Usuário
Na opção 3 vamos realizar uma atualização de endereço  do nosso usuário (Paulo Roberto) aqui como notável seguimos as orientações que o sistema (portal de reservas) nós fornece passamos nome do usuário para localizar, novo endereço rua 129, numeração 190 e estado Ceará no final as alterações foram salvas com sucesso.

![16062_192736_atualizando_dados_usuario1](https://github.com/user-attachments/assets/8d1010bd-060a-4a85-80a2-8aa2609a6487)

#### Visualização dos dados atualizados 
Como dito anteriormente as alterações foram salva no banco de dados é o que mostra a imagem acima no circulo vermelho.

![16062_192736_visualizando_usuarios2](https://github.com/user-attachments/assets/72e581e5-aa21-4dd9-a02b-d44f793c0f4c)

#### Deletando usuário no banco de dados
Para deleta o usuário no banco utilizamos a opção 4 e informamos o cpf para localiza o cadastro no banco na imagem acima passamos o cpf 666.888.999 - 11 como exemplo para excluir no final digitamos 2 para verificar se o usuário foi excluído no banco.

![16062_192736_excluido_usuario1](https://github.com/user-attachments/assets/8824f793-e653-47b9-abae-65f19d750950)

#### Visualizando destinos
Na opção 5 temos uma relações de todas os destinos cadastrado no banco são cerca de 5 destinos para os nossos usuários escolherem em cada destinos possui descrições breve sobre o perfis dos destinos.

![16062_192736_visualizando_destinos1](https://github.com/user-attachments/assets/ce94a405-9a9f-48a4-b037-d8e7a7f1d9cb)

#### Adicionando um novo destino
Para adiciona um novo destino ao banco utilizamos a opção 6 assim como as outras opções estamos seguidos as orientações para ilustra o destino que escolhemos foi a Estação das Docas do Estado do Pará e complementado com a sua descrição como é mostrado no círculo vermelho.

![16062_192736_adicionando_destino1](https://github.com/user-attachments/assets/e77e1c72-4647-4941-ac3c-a731dc8c2b2a)

#### Visualizado destino adicionado
Agora se voltamos na opção 5 veremos o nosso novo destino incluído com sucesso id 10 conforme é sublinha de vermelho.

![16062_192736_visualizando_destinos2](https://github.com/user-attachments/assets/157d5e87-c9b1-4b96-b5c8-87574f6278e1)

#### Deletando destino
Assim como temos a funcionalidade de excluir usuários também a para os destinos no opção 7 passamos o nome do destino que desejamos excluir do nosso banco viagens perceba o destino escolhido foi Brasílica do Senho do Borfim e para visualiza digitamos 5 como poder ser notável o destino foi excluído com sucesso.

![16062_192736_excluido_destino1](https://github.com/user-attachments/assets/7d976060-9a85-4500-acc4-c781511467d9)

#### Realizado reserva do usuário
Nessa imagem vamos realiza uma reserva com opção 8 de um usuário ( Aurora do Nascimento ) e seu destino e a Estação das Docas junto com seu status de confirmado e a data de realização 27/07/2024 e encerrado com a confirmação da reserva em destaque de circulo vermelho.

![16062_192736_realizada_reservas1](https://github.com/user-attachments/assets/7e093f5e-b199-4110-bb95-21cde6f25adb)


#### Usuários com reserva no banco
Na opção 9 vamos ter todos os usuários com reservas perceba que Aurora aparece com o id 6, o destino status e data de realização e por fim 
termos a ultima opção 10 que é para sai do sistema.

![16062_192736_visualizando_reserva_final1](https://github.com/user-attachments/assets/390f694d-8896-442d-8c4b-eb61d184c717)

### Conclusão:
Desenvolver o sistema com integração ao banco de dados mim proporcionou um crescimento significativo tanto como estudante e quanto pessoal os desafios enfrentados e as soluções implementadas contribuíram para criação de um sistema eficaz. Estou orgulhoso do trabalho realizando e dos aprendizados adquiridos ao longo do processo.
