from models.articulo import Articulo

class ArticuloController():

    def getAll():
        resp = []
        articulos = Articulo.query.all()
        for articulo in articulos:
            resp.append({
                "id": articulo.id,
                "nombre": articulo.nombre,
                "precio": articulo.precio,
                "iva": articulo.iva,
                "descripcion": articulo.descripcion,
                "image": articulo.image,
                "stock": articulo.stock,
                "id_Categorias": articulo.id_Categorias
            })
        return resp
    