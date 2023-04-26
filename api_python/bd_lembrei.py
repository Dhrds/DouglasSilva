import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="projetospark.com.br",
                                                user="u751391022_douglas",
                                                password="Admin123456",
                                                db="u751391022_douglas")
  
cursor = connection.cursor()
 
def conexao():
    connection = mysql.connector.connect(host="projetospark.com.br",
                                                user="u751391022_douglas",
                                                password="Admin123456",
                                                db="u751391022_douglas")
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

def insert_usuario(lista_values):
    connection = mysql.connector.connect(host="localhost",
                                    user="root",
                    
                                    password="123456",
                                    db="Lembrei")
    cursor = connection.cursor()
    try:
        if connection.is_connected():  
            cursor.execute("use lembrei")
            #print(f"""insert into lembrei (numero,usuario,senha,email) values {lista_values}; """)           
            cursor.execute(f"""insert into lembrei (numero,usuario,senha,email) values {lista_values}; """)
            connection.commit()
            cursor.close()              
            connection.close()
            return 'comitado'            
    except Error as e:
        return "usuario ou email ja usado", e

def insert_log_data(table,lista_coluna,lista_values):
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
    connection = mysql.connector.connect(host="projetospark.com.br",
                                                user="u751391022_douglas",
                                                password="Admin123456",
                                                db="u751391022_douglas")
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
     
def select_usuario (user):
    connection = mysql.connector.connect(host="projetospark.com.br",
                                                user="u751391022_douglas",
                                                password="Admin123456",
                                                db="u751391022_douglas")
    cursor = connection.cursor()
    try:
        if connection.is_connected():  
            cursor.execute("use u751391022_douglas")
            print(f"""select numero , email from lembrei where id = {user} """)            
            cursor.execute(f"""select numero , email from lembrei where id = {user} and e_rotina <> 'S' """)    
            db_inf = cursor.fetchall()                                        
            print('selecionado',db_inf)
            return db_inf
        else:
            print('nao')
    except Error as e:
        print("Erro ao conectar ao MySQL", e)        
            
def select_data (table):
    connection = mysql.connector.connect(host="projetospark.com.br",
                                                user="u751391022_douglas",
                                                password="Admin123456",
                                                db="u751391022_douglas")
    cursor = connection.cursor()
    try:
        if connection.is_connected():  
            cursor.execute("use u751391022_douglas") 
            cursor.execute("""select  DATE_FORMAT(data_hora,'%Y/%m/%d %T') ,id_usuario
                           , mensagem_aparecer,numero,email,e_rotina,id
                           from parametros_mensagem 
                           where data_hora = date_format(now(), '%Y-%m-%d  %H:%i') and e_rotina = 'N';""")            
            db_inf = cursor.fetchall()                                        
            print(db_inf)
            return db_inf
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
        
def alterar(id):
    connection = mysql.connector.connect(host="projetospark.com.br",
                                                user="u751391022_douglas",
                                                password="Admin123456",
                                                db="u751391022_douglas")
    cursor = connection.cursor()
    try:
        if connection.is_connected():  
            cursor.execute("use u751391022_douglas") 
            cursor.execute(f"""update parametros_mensagem set e_rotina = 'S' where id = {id};""")            
            db_inf = cursor.fetchall()                                        
            connection.commit()
            print('comitado')
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