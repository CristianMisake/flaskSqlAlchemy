from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    admin = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<Usuario %r>" % self.username

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<Categoria %r>" % self.nombre

class Articulo(db.Model):
    __tablename__ = 'articulos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    precio = db.Column(db.Integer, unique=True, nullable=False)
    iva = db.Column(db.Integer, unique=True, nullable=False)
    descripcion = db.Column(db.String(200), unique=True, nullable=False)
    image = db.Column(db.String(200), unique=True, nullable=False)
    stock = db.Column(db.Integer, unique=True, nullable=False)
    id_Categorias = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return "<Articulo %r>" % self.nombre

class Carrito(db.Model):
    __tablename__ = 'carrito'

    id = db.Column(db.Integer, primary_key=True)
    id_Articulos = db.Column(db.Integer, unique=True, nullable=False)
    id_Usuarios = db.Column(db.Integer, unique=True, nullable=False)
    cantidad = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return "<Carrito %r>" % self.id

if __name__=='__main__':
   app.run(debug=True)