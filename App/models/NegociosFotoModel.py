from App.extensions import SQLAlchemyBD

class NegociosFotos(SQLAlchemyBD.Model):
    __tablename__ = "NEGOCIOS_FOTOS"

    ID_FOTO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True)
    ID_NEGOCIO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('NEGOCIOS.ID_NEGOCIO'), nullable=False)
    FOTO = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=False)
    PORTADA = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    FECHAREG = SQLAlchemyBD.Column(SQLAlchemyBD.DateTime, nullable=False, default=SQLAlchemyBD.func.now())
    ACTIVA = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False, default=True)






