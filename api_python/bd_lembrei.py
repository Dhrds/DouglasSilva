import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="123456",
                                    db="Lembrei")
  
cursor = connection.cursor()

  
def conexao():
    connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="123456",
                                    db="Lembrei")
    cursor = connection.cursor()
    try:
        if connection.is_connected():  
            cursor = connection.cursor()            
            cursor.execute("select database();")
            db_inf = cursor.fetchone()
            print("Você está conectado ao banco de dados: ", db_inf)
        else:
            print('nao conectou')
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
  

def encerra():
    try:
        if connection.is_connected():              
            cursor.close()              
            connection.close()
            print('conexão encerrada')
        else:
            print('nao conectou')
            
    except Error as e:
        print("Erro ao conectar ao MySQL", e)



def insert(table,lista_coluna,lista_values):
    try:
        if connection.is_connected():  
            cursor.execute("use lembrei")
            print(f"""insert into {table} ({lista_coluna}) values ({lista_values}); """)            
            cursor.execute(f"""insert into {table} ({lista_coluna}) values ({lista_values}); """)
            connection.commit()
            print('comitado')
    except Error as e:
        print("Erro ao conectar ao MySQL", e)


def select (table):
    connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="123456",
                                    db="Lembrei")
    cursor = connection.cursor()
    try:
        if connection.is_connected():  
            cursor.execute("use lembrei")
            print(f"""select * from {table}  """)            
            cursor.execute(f"""select * from {table}  """)    
            db_inf = cursor.fetchall()                                        
            print('selecionado',db_inf)
            return db_inf
        else:
            print('nao')
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
            
def select_data (table):
    connection = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="123456",
                                    db="Lembrei")
    cursor = connection.cursor()
    try:
        if connection.is_connected():  
            cursor.execute("use lembrei") 
            cursor.execute("""select  DATE_FORMAT(data_hora,'%Y/%m/%d %T') 
                           from parametros_mensagem 
                           where data_hora = date_format(now(), '%Y-%m-%d  %H:%i');""")           
            #cursor.execute("""SELECT DATE_FORMAT(data_hora,'%Y/%m/%d %T') as data_f FROM parametros_mensagem """)  
            #select id_usuario, DATE_FORMAT(data_hora,'%Y/%m/%d %T') from parametros_mensagem where data_hora =   date_format(now(), '%Y-%m-%d  %H:%i');  
            db_inf = cursor.fetchall()                                        
            print(db_inf)
            return db_inf
    except Error as e:
        print("Erro ao conectar ao MySQL", e)

def delete (table,id):
    try:
        if connection.is_connected():  
            cursor.execute("use lembrei")
            print(f"""select * from {table} where id = {id} """)            
            cursor.execute(f"""select * from {table} where id = {id}  """)    
            db_inf = cursor.fetchall()    
            connection.commit()                                   
            print('selecionado',db_inf)
            return db_inf
    except Error as e:
        print("Erro ao conectar ao MySQL", e)           
            
if __name__ == "__main__":
    print  ('ok')