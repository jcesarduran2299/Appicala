from App.extensions import SQLAlchemyBD

class Usuario(SQLAlchemyBD.Model):
    __tablename__ = "USUARIOS"

    ID_USUARIO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True, autoincrement=True)
    CELULAR = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False)
    EMAIL = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), unique=True, nullable=False)
    NOMBRE = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), unique=True, nullable=False)
    CLAVE = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), unique=True, nullable=False)
    FECHAREG = SQLAlchemyBD.Column(SQLAlchemyBD.DateTime, nullable=False, server_default=SQLAlchemyBD.func.getdate())
    CODIGO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, unique=True, nullable=False)
    ADMINISTRADOR = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, unique=True, nullable=False)

    def __init__(self, nombre, email, celular, clave, codigo, administrador):
        self.NOMBRE = nombre
        self.EMAIL = email
        self.CELULAR = celular
        self.CLAVE = clave
        self.CODIGO = codigo
        self.ADMINISTRADOR = administrador

    def get_id(self):
        return f"{self.ID_USUARIO}_{self.NOMBRE}_Administrador"
        return str(self.ID_USUARIO), str(self.NOMBRE), str("Administrador")

    def save(self):
        SQLAlchemyBD.session.add(self)
        SQLAlchemyBD.session.commit()
    
    def is_active(self):
        return True
    
    @staticmethod
    def GetUserByEmail(IngresoEmail):
        return Usuario.query.filter_by(EMAIL=IngresoEmail).first()

