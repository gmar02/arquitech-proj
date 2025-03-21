from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from data import carregar_dados

###############################################################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schema.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
schema = SQLAlchemy(app)

###############################################################

class Usuario(schema.Model):

    __tablename__ = 'usuario'

    id = schema.Column(schema.Integer, primary_key=True)
    nome = schema.Column(schema.String(200), nullable=False)
    senha = schema.Column(schema.String(200), nullable=False)
    perfil = schema.Column(schema.String(1), nullable=False)

    def __repr__(self):
        return '<Usuário %r>' % self.id

###############################################################

@app.cli.command('inic_dados')
def inicializar_dados():

    print("Criando schema...")
    with app.app_context():
        schema.create_all()

    print("Carregando dados para o schema...")
    carregar_dados()

###############################################################

@app.route("/", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']

        usuario = Usuario.query.filter_by(nome=nome, senha=senha).first()
        if usuario:
            return redirect("/teste")
        
        return "Usuário e/ou senha inválidos", 401

    return render_template('login.html')

@app.route("/teste", methods=['GET'])
def teste():
    return "LOGIN REALIZADO COM SUCESSO"

###############################################################

if __name__ == "__main__":
    app.run(debug=True)
    