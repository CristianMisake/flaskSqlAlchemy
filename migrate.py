from app import db
from models.usuario import Usuario
from models.categoria import Categoria
from models.articulo import Articulo
from models.carrito import Carrito

db.create_all()

usuario1 = Usuario(username="juan", nombre="Juan Pacheco", email="juan@hotmail", admin="admin")
usuario2 = Usuario(username="tutu", nombre="Tutuneco Miranda", email="tutu@hotmail", admin="admin")
usuario3 = Usuario(username="kastor", nombre="KastorTroy", email="kastor@hotmail", admin="admin")

db.session.add(usuario1)
db.session.add(usuario2)
db.session.add(usuario3)

categoria1 = Categoria(nombre="Electrodomesticos")
categoria2 = Categoria(nombre="Utiles para el hogar")

db.session.add(categoria1)
db.session.add(categoria2)

articulo1 = Articulo(nombre="Nevera", precio=1200000, iva=0.19, descripcion="Nevera grante de doble puerta", image="nevera.jpg", stock=2, id_Categorias=1)
articulo2 = Articulo(nombre="Microndas", precio=400000, iva=0.19, descripcion="microndas de rapido calentado", image="microndas.jpg", stock=4, id_Categorias=1)
articulo3 = Articulo(nombre="Limpiador de ventanas", precio=10000, iva=0.19, descripcion="limpiador para ventanas", image="limpiador.jpg", stock=10, id_Categorias=2)

db.session.add(articulo1)
db.session.add(articulo2)
db.session.add(articulo3)

carrito1 = Carrito(id_Articulos=1, id_Usuarios=1, cantidad=1)

carrito2 = Carrito(id_Articulos=1, id_Usuarios=2, cantidad=1)
carrito3 = Carrito(id_Articulos=3, id_Usuarios=2, cantidad=3)

carrito4 = Carrito(id_Articulos=1, id_Usuarios=3, cantidad=1)
carrito5 = Carrito(id_Articulos=2, id_Usuarios=3, cantidad=1)
carrito6 = Carrito(id_Articulos=3, id_Usuarios=3, cantidad=1)

db.session.add(carrito1)
db.session.add(carrito2)
db.session.add(carrito3)
db.session.add(carrito4)
db.session.add(carrito5)
db.session.add(carrito6)

db.session.commit()
