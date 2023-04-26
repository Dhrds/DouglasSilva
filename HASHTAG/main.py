from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"
iduser = 0


@app.route('/<idade>', methods=['POST', 'GET'])
def login(idade):
    check = idade
    return render_template("index.html", msg=check)
    



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
    print(iduser)
    cad_msg = '51'
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
    print(iduser)
    cad_msg = 6515
    flash(cad_msg)
    return render_template("contatos.html", empresa=Empresa, cad_msg=cad_msg)


if __name__ == "__main__":
    app.run(debug=True)
