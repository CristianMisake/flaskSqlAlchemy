from models.categoria import Categoria

class CategoriaController():

    def getAll():
        resp = []
        categorias = Categoria.query.all()
        for categoria in categorias:
            resp.append({
                "id": categoria.id,
                "nombre": categoria.nombre,
            })
        return resp
    