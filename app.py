from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database = SQLAlchemy(app)

# tabela de membros do grupo, apenas para teste
class Membro(database.Model):
    
    __tablename__ = "membro"

    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(150), unique=True, nullable=False)
    matricula = database.Column(database.Integer, unique=True, nullable=True)
    email = database.Column(database.String(200), unique=True, nullable=True)

    def __repr__(self):
        return f"Membro(id = {self.id}, nome = {self.nome}, matricula = {self.matricula}, email = {self.email}"


@app.route("/")
def main():

    # obtendo todos os membros
    membros = Membro.query.all()

    return render_template('index.html', membros=membros)

