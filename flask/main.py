from flask import Flask, render_template, request,redirect ,flash
import bd_lembrei as bd
app = Flask(__name__)
app.config['SECRET_KEY']="123"
iduser = 0

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
            return redirect('/home')
        else:
            return render_template("index.html",msg = check)
    return render_template("index.html")        
    
@app.route('/autentificar',methods=['POST', 'GET'])
def autent():
    email = request.form.get('email_login')
    senha = request.form.get('senha_login')
    login = bd.select_usuario_login(email,senha)
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
        insert=(iduser,data+" "+hora+":00",email,phone,message)
        bd.insert_msg(insert)
    print(iduser)
    cad_msg = bd.select_msg(iduser)
    flash(cad_msg)
    return render_template("home.html", empresa=Empresa ,cad_msg = cad_msg )

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    Empresa = 'Lembrei'
    data = request.form.get('data')    
    hora = request.form.get('hora')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    if data != None:
        insert=(iduser,data+" "+hora+":00",email,phone,message)
        bd.insert_msg(insert)
    print(iduser)
    cad_msg = bd.select_msg(iduser)
    flash(cad_msg)
    return render_template("contatos.html", empresa=Empresa ,cad_msg = cad_msg )

if __name__ == "__main__":
    app.run(debug=True)
