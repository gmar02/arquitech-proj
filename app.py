from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

###############################################################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schema.db'
schema = SQLAlchemy(app)

###############################################################

class Usuario(schema.Model):
    id = schema.Column(schema.Integer, primary_key=True)
    nome = schema.Column(schema.String(200), nullable=False)
    perfil = schema.Column(schema.String(1), nullable=False)
    senha = schema.Column(schema.String(200), nullable=False)

    def __repr__(self):
        return '<Usuário %r>' % self.id

###############################################################

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

###############################################################

if __name__ == "__main__":
    
    with app.app_context():
        schema.create_all()

    app.run(debug=True)
