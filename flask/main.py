from flask import Flask, render_template, request
import bd_lembrei as bd
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    usuario = request.form.get('nome_cad')
    senha = request.form.get('senha_cad')
    email = request.form.get('email_cad')
    numero = request.form.get('tel_cad')
    cad =(numero,usuario,senha,email)
    if cad != (None, None, None, None):
        check = bd.insert_usuario(cad)
        if check == True:
            print(1)
            return render_template("index.html")
        else:
            print(2)
            return render_template("index.html")
    email = request.form.get('email_login')
    senha = request.form.get('senha_login')
    login = bd.select_usuario_login(email,senha)
    if login != []:
        print(3)
        return render_template("index.html")
    else:
        print(4)
        return render_template("index.html")        
    
    

@app.route('/home')
def contatos():
    return render_template("home.html")


app.run(debug=True)
