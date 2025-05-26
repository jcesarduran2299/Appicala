from flask_login import UserMixin

class AuthUser(UserMixin):
    def __init__(self, id, nombre, tipo, foto):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.foto = foto

    def get_id(self):
        return self.id, self.nombre, self.tipo, self.foto
        return f"{self.id}_{self.nombre}_{self.tipo}"

    @property
    def is_authenticated(self):
        return True

    def is_active(self):
        return True