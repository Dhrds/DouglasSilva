import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="123456",
                                    db="Lembrei")
  
cursor = connection.cursor()

class conexao():   
    def __init__(self):
        try:
           if connection.is_connected():              
              cursor.execute("select database();")
              db_inf = cursor.fetchone()
              print("Você está conectado ao banco de dados: ", db_inf)
        except Error as e:
            print("Erro ao conectar ao MySQL", e)
  
class encerra():
    def __init__(self):
        try:
           if connection.is_connected():              
              cursor.close()              
              connection.close()
              print('conexão encerrada')
              
        except Error as e:
            print("Erro ao conectar ao MySQL", e)


class insert_bd():   
    def insert(table,lista_coluna,lista_values):
        try:
           if connection.is_connected():  
              cursor.execute("use lembrei")
              print(f"""insert into {table} ({lista_coluna}) values (11,{lista_values}); """)            
              cursor.execute(f"""insert into {table} ({lista_coluna}) values ({lista_values}); """)
              connection.commit()
              print('comitado')
        except Error as e:
            print("Erro ao conectar ao MySQL", e)

conexao()
tabela = 'lembrei'
colunas = 'numero,usuario,senha'
values='"+5537999775765","teste21","123"'
insert_bd.insert(table=tabela,lista_coluna=colunas,lista_values=values)