from App.extensions import SQLAlchemyBD

class PedidosEstados(SQLAlchemyBD.Model):
    __tablename__ = "PEDIDOS_ESTADOS"

    ID_ESTADO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True)
    ESTADO_PEDIDO = SQLAlchemyBD.Column(SQLAlchemyBD.String(20), nullable=False)





