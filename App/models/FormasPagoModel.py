from App.extensions import SQLAlchemyBD

class FormasPago(SQLAlchemyBD.Model):
    __tablename__ = "FORMAS_PAGO"

    ID_FPAGO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True)
    FORMA_PAGO = SQLAlchemyBD.Column(SQLAlchemyBD.String(20), nullable=False)









