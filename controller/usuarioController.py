from models.usuario import Usuario

class UsuarioController():

    def getAll():
        resp = []
        usuarios = Usuario.query.all()
        for usuario in usuarios:
            resp.append({
                "id": usuario.id,
                "username": usuario.username,
                "nombre": usuario.nombre,
                "email": usuario.email,
                "admin": usuario.admin
            })
        return resp
    