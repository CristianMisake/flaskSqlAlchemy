from app import db

class Carrito(db.Model):
    __tablename__ = 'carrito'

    id = db.Column(db.Integer, primary_key=True)
    id_Articulos = db.Column(db.Integer, nullable=False)
    id_Usuarios = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Carrito %r>" % self.id