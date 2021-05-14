from app import db

class Articulo(db.Model):
    __tablename__ = 'articulos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    iva = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    id_Categorias = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Articulo %r>" % self.nombre