import sqlite3 as conector


def Tabela_Usuario(tabela_usuario_nome, tabela_usuario_cpf, tabela_usuario_data_nascimento, tabela_usuario_endereco_email, tabela_usuario_rua, tabela_usuario_cidada, tabela_usuario_numero, tabela_usuario_estado):
 conexao = conector.connect("viagens.db")
 curson = conexao.cursor()

# criação da tabela usuário se não existir
 curson.execute('''CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT(255),
               cpf INTEGER,
               data_nascimento INTERGER,
               endereco_email INTERGER,
               rua VARCHAR(255),
               cidade TEXT(150),
               numero INTEGER,
               estado TEXT(60) 
)''')


# inserir registros na tabela usuários
# realizar uma consulta
 curson.execute("INSERT INTO usuarios (nome, cpf, data_nascimento, endereco_email, rua, cidade, numero, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (tabela_usuario_nome, tabela_usuario_cpf, tabela_usuario_data_nascimento, tabela_usuario_endereco_email, tabela_usuario_rua, tabela_usuario_cidada, tabela_usuario_numero, tabela_usuario_estado))
 print("Novo usuário cadastrado com sucesso!")
 # salvando as alterações no banco
 conexao.commit()
#  menu de opções
 Menu()

def Tabela_Destinos(tabela_destino_nome_destino, tabela_destino_descricao_destino):
 conexao = conector.connect("viagens.db")
 curson = conexao.cursor()

 # criação da tabela destinos se não existir
 curson.execute('''CREATE TABLE IF NOT EXISTS destinos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT(255),
               descricao VARCHAR(60) 
)''')

 curson.execute("INSERT INTO destinos (nome, descricao) VALUES (?, ?)", (tabela_destino_nome_destino, tabela_destino_descricao_destino))
 print("novo destino cadastrado com sucesso !")
 # salvando as alterações no banco
 conexao.commit()
#  menu de opções
 Menu()


def Realizar_Reservas():
  print("".center(90,"-"))
  print( """     PARA REALIZAR A RESERVA DO CLIENTE SIGA AS ORIENTAÇÕES ABAIXO:
                             1. Informe o nome complento do cliente
                             2. Informe o nome completo do destino 
         """
      )
  nome_usuario = input("digiter o nome: ")
  nome_destino = input("digiter o nome do destino: ")
  status_destino = input("Digiter o status: ")
  data_reserva = input("digiter a data da reserva: ")
  Tabela_Reservas(nome_usuario, nome_destino, status_destino, data_reserva)

def Tabela_Reservas(tabela_reservas_nome_usuario, tabela_reservas_nome_destino, tabela_reservas_status_destino, tabela_reservas_data_reserva):
 conexao = conector.connect("viagens.db")
#  conexao.execute("PRAGMA foreign_keys = on")
 curson = conexao.cursor()
# criação da tabela reservas se não existir
 curson.execute('''CREATE TABLE IF NOT EXISTS reserva(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome_usuario TEXT(60), 
               nome_destinos TEXT(60),
               status,
               data DATE 
)''')
 curson.execute("INSERT INTO reservas (id_usuario, id_destino, status, data) VALUES (?, ?, ?, ?)", (tabela_reservas_nome_usuario, tabela_reservas_nome_destino, tabela_reservas_status_destino, tabela_reservas_data_reserva))
 conexao.commit()
 print(f"A reserva de {tabela_reservas_nome_usuario} para {tabela_reservas_nome_destino} foi confirmada com sucesso !")
 Menu()


def Visualizar_Reservas():
  conexao = conector.connect("viagens.db")
  curson = conexao.cursor()
  curson.execute('''SELECT * FROM reservas
                 ''')
  for registro in curson.fetchall():
      print("usuários com reservas")
      print(registro)
#  menu de opções
  Menu()

# exclui um usuário
def Excluir_Cadastro_Usuarios(curson, conexao):
 cpf_apagar = input("digiter o cpf do cliente: ")
 curson.execute("DELETE FROM usuarios where cpf = ?", (cpf_apagar,))
 conexao.commit()
 print("cadastro do usuário deletado com sucesso")
 print("digiter [2]: para visualizar")
 botao_de_manipulacao = int(input("digiter: "))
 match botao_de_manipulacao:
    case 2:
     Consulta_Usuarios()
     Menu()


# exclui um usuário
def Excluir_Cadastro_Destino(curson, conexao):
 nome_apagar_destino = input("digiter o nome:: ")
 curson.execute("DELETE FROM destinos where nome = ?", (nome_apagar_destino,))
 conexao.commit()
 print("destino excluído com sucesso no banco!")
 print("digiter [5]: para visualizar")
 botao_de_manipulacao =  int(input("digiter: "))
 match botao_de_manipulacao:
    case 5:
     Consulta_Destinos()
     Menu()

# atualiza dados do cliente
def Atualiza_Dados(conexao, curson):
  print("".center(90,"-"))
  print("""PARA ATUALIZAR O ENDEREÇO DO USUÁRIO SIGA AS INSTRUÇÕES ABAIXO:
                1. Informe o nome do usuário para localiza no banco.
                2. Informe a numeração da residência.
                3. Informe a cidade.
                4. Informe o estado.
        """)
  nome_atualizar = input("digiter o nome: ")
# atualizando o endereço
  rua_atualizar = input("informe o nome da rua: ")
  numero_atualizar = input("informe a numeração da residência: ")
  cidade_atualizar = input("informe a cidade: ")
  estado_atualizar = input("informe o estado: ")
  curson.execute("UPDATE usuarios SET rua = ? where nome = ?" , (rua_atualizar, nome_atualizar))
  curson.execute("UPDATE usuarios SET cidade = ? where nome = ?", (cidade_atualizar, nome_atualizar))
  curson.execute("UPDATE usuarios SET numero = ? where nome = ?", (numero_atualizar, nome_atualizar,))
  curson.execute("UPDATE usuarios SET estado = ? where nome = ?", (estado_atualizar, nome_atualizar,))
# salvando as alterações no banco
  conexao.commit()
  print("alterações salva com sucesso !")
  Menu()


# coleta de dados para cadastro de novos clientes
def Coleta_Dados_Usuarios():
   print("".center(90,"-"))
   print( """     PARA REALIZAR CADASTRO DO CLIENTE SIGA AS ORIENTAÇÕES ABAIXO:
                             1. Informe o nome complento
                             2. Informe o cpf: xxx.xxx.xxx - xx
                             3. Data de nascimento: dia/mes/ano
                             4. Endereço de e-mail: endereco@gmail.com
                             5. Endereço da residencia: rua, cidade, numero, estado
         """
      )
   nome = input("digiter o nome: ")
   cpf = input("digiter o cpf: ")
   data_nascimento = input("digiter a data de nasciemento: ")
   endereco_email = input("digiter o endereço de e-mail: ")
   rua = input("digiter o nome da rua: ")
   cidada = input("digiter o nome da cidade: ")
   numero = input("digiter o numero da casa: ")
   estado = input("digiter o nome do estado: ")
   Tabela_Usuario(nome, cpf, data_nascimento, endereco_email, rua, cidada, numero, estado)

# coleta de dados para cadastro de novos lugares
def Coleta_Dados_Destinos():
  print("".center(90,"-"))
  print( """     PARA REALIZAR CADASTRO DE LUGAR SIGA AS ORIENTAÇÕES ABAIXO:
                             1. Informe o nome complento
                             2. Informe o a sua descrição
         """
      )
  nome_destino = input("digiter o nome: ")
  descricao_destino = input("digiter o descrição: ")
  Tabela_Destinos(nome_destino, descricao_destino)


# consulta usuarios
def Consulta_Usuarios():
  conexao = conector.connect("viagens.db")
  curson = conexao.cursor()
  curson.execute("SELECT *FROM usuarios")
  print("usuários cadastrados no banco")
  for registro in curson.fetchall():
      print(registro)

# consulta destinos
def Consulta_Destinos():
  conexao = conector.connect("viagens.db")
  curson = conexao.cursor()
  curson.execute("SELECT *FROM destinos")
  print("destinos cadastrados no sistema")
  for registro in curson.fetchall():
      print(registro)

  
def Sair():
  print("você saiu do sistema")

  
def Verificar_Botao(botao):
 match botao:
     case 1:
      Coleta_Dados_Usuarios()
     case 2:
        Consulta_Usuarios()
        Menu()
     case 3:
      conexao = conector.connect("viagens.db")
      curson = conexao.cursor()
      Atualiza_Dados(conexao, curson)
     case 4:
      conexao = conector.connect("viagens.db")
      curson = conexao.cursor()
      Excluir_Cadastro_Usuarios(curson, conexao)
     case 5:
      Consulta_Destinos()
      Menu()
     case 6:
       Coleta_Dados_Destinos()
     case 7:
       conexao = conector.connect("viagens.db")
       curson = conexao.cursor()
       Excluir_Cadastro_Destino(curson, conexao)
     case 8:
       Realizar_Reservas()
     case 9:
      Visualizar_Reservas()
     case 10:
      Sair()
           

# menu de opções
def Menu():
  print("".center(90,"-"))
  print("""          Menu
      1. Digiter [1] para realizar cadastro.
      2. Digiter [2] para ver os usuários cadastrados.
      3. Digiter [3] para atualiza o endereço.
      4. Digiter [4] para excluir um cadastro.
      5. Digiter [5] para vizualizar todos os destinos.
      6. Digiter [6] para adicionar um novo destino.
      7. Digiter [7] para excluir um destino.
      8. Digiter [8] para realizar uma reserva.
      9. Digiter [9] para visualizar as reservas.
      10.Digiter [10] para sair do sistema.
      """)
  botao = int(input("Digiter uma opção: "))
  Verificar_Botao(botao)


# tela de acesso
def Acessar_Sistema():
 print("".center(90,"-"))
 print("""BEM VINDO AO PORTAL DE VIAGENS
      siga as orientações abaixo:
      1. Digiter [1] para realizar cadastro.
      2. Digiter [2] para ver os usuários cadastrados.
      3. Digiter [3] para atualiza o endereço.
      4. Digiter [4] para excluir um cadastro.
      5. Digiter [5] para vizualizar todos os destinos.
      6. Digiter [6] para adicionar um novo destino.
      7. Digiter [7] para excluir um destino.
      8. Digiter [8] para realizar uma reserva.
      9. Digiter [9] para visualizar as reservas.
      10.Digiter [10] para sair do sistema. 
      """)
 botao = int(input("Digiter uma opção: "))
# chamanda da função verificar_botao
 Verificar_Botao(botao)
Acessar_Sistema()