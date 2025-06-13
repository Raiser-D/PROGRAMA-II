from flask import url_for
from config import *
from model import *
from pony.orm import db_session, commit

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    with db_session:
        # obtém as pessoas
        pessoas = Pessoa.select() 
        return render_template("listar_pessoas.html", pessoas=pessoas)

@app.route("/form_adicionar_pessoa")
def form_adicionar_pessoa():
    return render_template("form_adicionar_pessoa.html")

@app.route("/cadastrar_pessoa", methods=["GET", "POST"])
def cadastrar_pessoa():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        rg = request.form.get("registro_geral")
        dt_nasc = request.form.get("dt_nasc")
        if not dt_nasc:
           dt_nasc = '2000-01-01'
        cep = request.form.get("cep")
        rua = request.form.get("rua")
        bairro = request.form.get("bairro")
        num_casa = request.form.get("num_casa")
        peso = request.form.get("peso")

        with db_session:
            Pessoa(
                nome=nome,
                email=email,
                telefone=telefone,
                cpf=cpf,
                rg=rg,
                dt_nasc=dt_nasc,
                cep=cep,
                rua=rua,
                bairro=bairro,
                num_casa=int(num_casa),
                peso=float(peso)
            )
            commit()
        return redirect(url_for('listar_pessoas'))
    
    return render_template("form_adicionar_pessoa.html")

if __name__ == "__main__":
    app.run(debug=True)

'''
run:
$ flask run
'''
