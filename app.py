################################  IMPORTAÇÕES  ################################

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from data import carregar_dados

###############################  CONFIGURAÇÕES  ###############################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schema.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
schema = SQLAlchemy(app)

#################################  ENTIDADES  #################################

class Usuario(schema.Model):

    __tablename__ = 'usuario'

    id = schema.Column(schema.Integer, primary_key=True)
    nome = schema.Column(schema.String(200), nullable=False)
    senha = schema.Column(schema.String(200), nullable=False)
    perfil = schema.Column(schema.String(1), nullable=False)

    def __repr__(self):
        return '<Usuário %r>' % self.id


class Post(schema.Model):

    __tablename__ = 'post'

    id = schema.Column(schema.Integer, primary_key=True)
    titulo = schema.Column(schema.String(300), nullable=False) 
    subtitulo = schema.Column(schema.String(500), nullable=False)
    corpo = schema.Column(schema.Text, nullable=False)
    modelo3d = schema.Column(schema.LargeBinary, nullable=True)

    # Relacionamento com tabela de Usuário
    id_autor = schema.Column(schema.Integer, schema.ForeignKey('usuario.id'), nullable=False)
    autor = schema.relationship('Usuario', backref='posts')

    def __repr__(self):
        return "<Post %r>" % self.id

################################  COMANDOS CLI  ###############################

@app.cli.command('inic_dados')
def inicializar_dados():

    print("Criando schema...")
    with app.app_context():
        schema.create_all()
        print("Schema criado com sucesso!")

    print("Carregando dados para o schema...")
    carregar_dados()

###################################  ROTAS  ###################################

@app.route("/", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']

        usuario = Usuario.query.filter_by(nome=nome, senha=senha).first()
        
        if usuario:

            if usuario.perfil == 'A':
                return redirect(f"/autor/{usuario.id}")

            return redirect(f"/leitor/{usuario.id}")
        
        return "Usuário e/ou senha inválidos", 401

    return render_template('login.html')

@app.route("/autor/<int:id>", methods=['GET'])
def hub_autor(id):

    # Obtendo Usuário
    usuario = Usuario.query.get(id)

    if usuario:
        # Obtendo lista de posts do usuario (autor)
        posts_do_usuario = Post.query.filter_by(id_autor=id).all()
        return render_template('autor.html', autor=usuario, posts_do_autor=posts_do_usuario)

    return f"Usuário de id {id} não encontrado.", 404

@app.route("/leitor/<int:id>", methods=['GET'])
def hub_leitor(id):
    return f"BEM VINDO À PÁGINA DO LEITOR! ID: {id}"

###################################  EXTRA  ###################################

if __name__ == "__main__":
    app.run(debug=True)
