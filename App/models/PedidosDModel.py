from App.extensions import SQLAlchemyBD

class PedidosD(SQLAlchemyBD.Model):
    __tablename__ = "PEDIDOSD"

    ID = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True)
    ID_PEDIDO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('PEDIDOSM.ID_PEDIDO'), nullable=False)
    ID_PRODUCTO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('NEGOCIOS_PRODUCTOS.ID_PRODUCTO'), nullable=False)
    CANTIDAD = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, nullable=False, default=1)
    PRECIO = SQLAlchemyBD.Column(SQLAlchemyBD.Numeric(18, 2), nullable=False)
    TOTAL = SQLAlchemyBD.column_property(CANTIDAD * PRECIO)
    OBSERVACIONES = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=True)





