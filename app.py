from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')
    
from controller.usuarioController import UsuarioController
from controller.categoriaController import CategoriaController
from controller.articuloController import ArticuloController

@app.route('/usuarios')
def getUsuarios():
    return jsonify({ "usuarios": UsuarioController.getAll() })

@app.route('/categorias')
def getCategorias():
    return jsonify({ "categorias": CategoriaController.getAll() })

@app.route('/articulos')
def getArticulos():
    return jsonify({ "articulos": ArticuloController.getAll() })

if __name__=='__main__':
   app.run(debug=True)