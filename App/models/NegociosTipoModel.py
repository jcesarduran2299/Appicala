from App.extensions import SQLAlchemyBD

class NegociosTipo(SQLAlchemyBD.Model):
    __tablename__ = "NEGOCIOS_TIPO"

    ID_TIPO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True)
    TIPO = SQLAlchemyBD.Column(SQLAlchemyBD.String(30), nullable=False)
    ICONO = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=True)
    TIPOCARD = SQLAlchemyBD.Column(SQLAlchemyBD.String(50), nullable=True)





