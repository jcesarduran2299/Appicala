from App.extensions import SQLAlchemyBD

class Negocios(SQLAlchemyBD.Model):
    __tablename__ = "NEGOCIOS"
    
    ID_NEGOCIO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True, autoincrement=True)
    ID_TIPO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, nullable=False)
    NOMBRE = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=False)
    DIRECCION = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=False)
    CELULAR = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False)
    WHATSAPP = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False)
    FACEBOOK = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    INSTAGRAM = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    EMAIL = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    DESCRIPCION = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=False)
    INFORMACION = SQLAlchemyBD.Column(SQLAlchemyBD.String(1000), nullable=False)
    CALIFICACION = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, nullable=False)
    LIKES = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, nullable=False)
    LATITUD = SQLAlchemyBD.Column(SQLAlchemyBD.Float, nullable=False)
    LONGITUD = SQLAlchemyBD.Column(SQLAlchemyBD.Float, nullable=False)
    FECHAREG = SQLAlchemyBD.Column(SQLAlchemyBD.DateTime, nullable=False, server_default=SQLAlchemyBD.func.getdate())
    ACTIVO = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    ID_USUARIO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('USUARIOS.ID_USUARIO'), nullable=False)
    FOTO = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), nullable=False)
    ID_PLAN = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, nullable=False)
    FECHA_ULTIMO_PAGO = SQLAlchemyBD.Column(SQLAlchemyBD.Date, nullable=False)
    FECHA_ACTIVO = SQLAlchemyBD.Column(SQLAlchemyBD.Date, nullable=False)
    CONSECUTIVO_PEDIDOS = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, nullable=False)
    RUT = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    IDENTIFICACION_RL = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    CERT_BANCARIA = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    LOGO = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), nullable=False)
    DESTACADO = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    HORARIO = SQLAlchemyBD.Column(SQLAlchemyBD.String(200), nullable=False)
    DOMICILIOS = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    ABIERTO = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    SALDO = SQLAlchemyBD.Column(SQLAlchemyBD.Numeric(18, 2), nullable=False)
    USUARIO = SQLAlchemyBD.Column(SQLAlchemyBD.String(20), nullable=False)
    CLAVE = SQLAlchemyBD.Column(SQLAlchemyBD.String(20), nullable=False)
    NEQUI = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    CUENTA_NEQUI = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False)
    DAVIPLATA = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    CUENTA_DAVIPLATA = SQLAlchemyBD.Column(SQLAlchemyBD.String(10), nullable=False)
    BANCOLOMBIA = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, nullable=False)
    CUENTA_BANCOLOMBIA = SQLAlchemyBD.Column(SQLAlchemyBD.String(20), nullable=False)
    PALABRAS_CLAVE = SQLAlchemyBD.Column(SQLAlchemyBD.String(200), nullable=False)

    def get_id(self):
        return str(self.ID_NEGOCIO), str(self.NOMBRE), str("Cliente")

    def save(self):
        SQLAlchemyBD.session.add(self)
        SQLAlchemyBD.session.commit()
    
    def is_active(self):
        return True
    
    @staticmethod
    def GetUserByUser(IngresoUser):
        return Negocios.query.filter_by(USUARIO=IngresoUser).first()

