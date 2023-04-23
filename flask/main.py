from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"
iduser = 0

import mysql.connector
from mysql.connector import Error
import time


class bd():
    def select_usuario_login(email, senha):
        connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="123456",
                                             db="lembrei")
        cursor = connection.cursor()
        try:
            if connection.is_connected():
                cursor.execute("use lembrei")
                cursor.execute(
                    f"""select id from lembrei where email = '{email}' and senha = '{senha}'  """)
                db_inf = cursor.fetchall()
                print(db_inf)
                return db_inf
            else:
                print('nao')
        except Error as e:
            print("Erro ao conectar ao MySQL", e)

    def select_msg(id):
        connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="123456",
                                             db="lembrei")
        cursor = connection.cursor()
        try:
            if connection.is_connected():
                cursor.execute("use lembrei")
                cursor.execute(
                    f"""select p.data_hora,p.email,p.numero,p.mensagem_aparecer 
                    from parametros_mensagem p
                    where id_usuario = {id}  """)
                db_inf = cursor.fetchall()
                print(db_inf)
                return db_inf
            else:
                print('nao')
        except Error as e:
            print("Erro ao conectar ao MySQL", e)

    def insert_msg(lista_values):
        connection = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="123456",
                                             db="lembrei")
        cursor = connection.cursor()
        try:
            if connection.is_connected():
                cursor.execute("use lembrei")
                print(
                    f"""insert into parametros_mensagem (id_usuario,data_hora,email, numero,mensagem_aparecer) values {lista_values} ; """)
                cursor.execute(
                    f"""insert into parametros_mensagem
                    (id_usuario,data_hora,email, numero,mensagem_aparecer)
                    values {lista_values} ; """)
                connection.commit()
                cursor.close()
                connection.close()
                print('comitado')
                return True
        except Error as e:
            print("usuario ou email ja usado", e)
            return "usuario ou email ja usado"

    def insert_usuario(lista_values):
        connection = mysql.connector.connect(host="localhost",
                                                user="root",
                                                password="123456",
                                                db="lembrei")
        cursor = connection.cursor()
        try:
            if connection.is_connected():
                cursor.execute("use lembrei")
                cursor.execute(
                    f"""insert into lembrei (numero,usuario,senha,email) values {lista_values}; """)
                connection.commit()
                cursor.close()
                connection.close()
                print('comitado')
                return True
        except Error as e:
            print("usuario ou email ja usado", e)
            return "usuario ou email ja usado"

@app.route('/', methods=['POST', 'GET'])
def login():
    usuario = request.form.get('nome_cad')
    senha = request.form.get('senha_cad')
    email = request.form.get('email_cad')
    numero = request.form.get('tel_cad')
    cad = (numero, usuario, senha, email)
    print(cad)
    if cad != (None, None, None, None):
        check = bd.insert_usuario(cad)
        if check == True:
            return redirect('/#paralogin')
        else:
            return render_template("index.html", msg=check)
    return render_template("index.html")


@app.route('/autentificar', methods=['POST', 'GET'])
def autent():
    email = request.form.get('email_login')
    senha = request.form.get('senha_login')
    login = bd.select_usuario_login(email, senha)
    if login != []:
        global iduser
        iduser = login[0][0]
        return redirect('/home')
    else:
        return redirect('/#paralogin')


@app.route('/home', methods=['POST', 'GET'])
def home():
    Empresa = 'Lembrei'
    data = request.form.get('data')
    hora = request.form.get('hora')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    if data != None:
        insert = (iduser, data + " " + hora + ":00", email, phone, message)
        bd.insert_msg(insert)
    print(iduser)
    cad_msg = bd.select_msg(iduser)
    flash(cad_msg)
    return render_template("home.html", empresa=Empresa, cad_msg=cad_msg)


@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    Empresa = 'Lembrei'
    data = request.form.get('data')
    hora = request.form.get('hora')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    if data != None:
        insert = (iduser, data + " " + hora + ":00", email, phone, message)
        bd.insert_msg(insert)
    print(iduser)
    cad_msg = bd.select_msg(iduser)
    flash(cad_msg)
    return render_template("contatos.html", empresa=Empresa, cad_msg=cad_msg)


if __name__ == "__main__":
    app.run(debug=True)
