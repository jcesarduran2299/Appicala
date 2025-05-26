from App.extensions import SQLAlchemyBD

class Visitantes(SQLAlchemyBD.Model):
    __tablename__ = "VISITANTES"

    ID_VISITANTE = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True)
    CELULAR = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False)
    NOMBRE = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    EMAIL = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    FECHAREG = SQLAlchemyBD.Column(SQLAlchemyBD.DateTime, nullable=False, server_default=SQLAlchemyBD.func.getdate())
    CODIGO_ACTIVACION = SQLAlchemyBD.Column(SQLAlchemyBD.String(6), nullable=False)
    ACTIVO = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False, default=False)
    REGISTRADO = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False, default=False)
    TOKEN = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=True)
    DIRECCION = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=True)
    LATITUD = SQLAlchemyBD.Column(SQLAlchemyBD.Float, nullable=True)
    LONGITUD = SQLAlchemyBD.Column(SQLAlchemyBD.Float, nullable=True)
    CLAVE = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False, default='123')
    USUARIO = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False, unique=True)




