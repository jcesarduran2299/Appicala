from App.extensions import SQLAlchemyBD

class NegociosProductos(SQLAlchemyBD.Model):
    __tablename__ = "NEGOCIOS_PRODUCTOS"

    ID_PRODUCTO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True)
    ID_NEGOCIO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('NEGOCIOS.ID_NEGOCIO'), nullable=False)
    PRODUCTO = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    DESCRIPCION = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=False)
    FOTO = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=False)
    PRECIO = SQLAlchemyBD.Column(SQLAlchemyBD.Numeric(18, 2), nullable=False)
    ACTIVO = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False, default=True)
