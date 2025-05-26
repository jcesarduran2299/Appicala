from App.extensions import SQLAlchemyBD
from sqlalchemy.sql import func
from App.functions import *
from App.models.PedidosDModel import PedidosD
from App.models.VisitantesModel import Visitantes
from App.models.PedidosEstadosModel import PedidosEstados
from App.models.FormasPagoModel import FormasPago
from App.models.NegociosProductosModel import NegociosProductos


class PedidosM(SQLAlchemyBD.Model):
    __tablename__ = "PEDIDOSM"

    ID_PEDIDO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, primary_key=True, autoincrement=True)
    ID_VISITANTE = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('VISITANTES.ID_VISITANTE'), nullable=False)
    ID_NEGOCIO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('NEGOCIOS.ID_NEGOCIO'), nullable=False)
    FECHA_REGISTRO = SQLAlchemyBD.Column(SQLAlchemyBD.DateTime, nullable=False, server_default=SQLAlchemyBD.func.getdate())
    ID_ESTADO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('PEDIDOS_ESTADOS.ID_ESTADO'), nullable=False)
    VALOR = SQLAlchemyBD.Column(SQLAlchemyBD.Numeric(18, 2), nullable=False)
    LATITUD = SQLAlchemyBD.Column(SQLAlchemyBD.Float, nullable=False)
    LONGITUD = SQLAlchemyBD.Column(SQLAlchemyBD.Float, nullable=False)
    TOTAL = SQLAlchemyBD.Column(SQLAlchemyBD.Numeric(18, 2), nullable=False)
    DIRECCION = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), unique=True, nullable=False)
    PAGADO = SQLAlchemyBD.Column(SQLAlchemyBD.Boolean, unique=True, nullable=False)
    ID_FPAGO = SQLAlchemyBD.Column(SQLAlchemyBD.Integer, SQLAlchemyBD.ForeignKey('FORMAS_PAGO.ID_FPAGO'), nullable=False)
    OBSERVACIONES = SQLAlchemyBD.Column(SQLAlchemyBD.String(300), unique=True, nullable=False)
    COMPROBANTE = SQLAlchemyBD.Column(SQLAlchemyBD.String(100), unique=True, nullable=False)

    @classmethod
    def ObtenerCuentaPedidosClient(cls, NegocioId):
        #Consultar por estado la cuenta de los pedidos, EN ESPERA, EN PREPARACION, EN CAMINO, ENTREGADO
        try:
            CuentaPedidosPorEstadoSeparado = SQLAlchemyBD.session.query(
                cls.ID_ESTADO,
                PedidosEstados.ESTADO_PEDIDO,
                func.count(cls.ID_PEDIDO).label("TOTAL_PEDIDOS")
            ).join(PedidosEstados, cls.ID_ESTADO == PedidosEstados.ID_ESTADO)\
             .filter(cls.ID_NEGOCIO == NegocioId)\
             .group_by(cls.ID_ESTADO, PedidosEstados.ESTADO_PEDIDO).all()
            return CuentaPedidosPorEstadoSeparado
        except Exception as e:
            print(f"Error en la linea {sys.exc_info()[-1].tb_lineno} de ObtenerCuentaPedidosClient: {e}")
            return False

    @classmethod
    def ObtenerPedidosWithDetalle(cls, NegocioId, SearchState=None):
        subquery = SQLAlchemyBD.session.query(
            PedidosD.ID_PEDIDO,
            func.count(PedidosD.ID_PRODUCTO).label("TOTAL_PRODUCTOS")
        ).group_by(PedidosD.ID_PEDIDO).subquery()

        query = SQLAlchemyBD.session.query(
            cls.ID_PEDIDO,
            cls.ID_VISITANTE,
            cls.ID_NEGOCIO,
            cls.FECHA_REGISTRO,
            cls.ID_ESTADO,
            PedidosEstados.ESTADO_PEDIDO,
            cls.VALOR,
            cls.LATITUD,
            cls.LONGITUD,
            cls.TOTAL,
            cls.DIRECCION,
            cls.PAGADO,
            cls.ID_FPAGO,
            FormasPago.FORMA_PAGO,
            cls.OBSERVACIONES,
            cls.COMPROBANTE,
            Visitantes.ID_VISITANTE,
            Visitantes.CELULAR,
            Visitantes.NOMBRE,
            Visitantes.EMAIL,
            subquery.c.TOTAL_PRODUCTOS
        ).join(Visitantes, cls.ID_VISITANTE == Visitantes.ID_VISITANTE)\
         .join(PedidosEstados, cls.ID_ESTADO == PedidosEstados.ID_ESTADO)\
         .join(FormasPago, cls.ID_FPAGO == FormasPago.ID_FPAGO)\
         .outerjoin(subquery, cls.ID_PEDIDO == subquery.c.ID_PEDIDO)\
         .filter(cls.ID_NEGOCIO == NegocioId, PedidosEstados.ESTADO_PEDIDO == SearchState)

        return query.all()

    @classmethod
    def UpdatePedidosStatusCliente(cls, NegocioId, PedidoId, EstadoName):
        try:
            Pedido = cls.query.filter_by(ID_NEGOCIO=NegocioId).filter_by(ID_PEDIDO=PedidoId).first()
            Pedido.ID_ESTADO = (PedidosEstados.query.filter_by(ESTADO_PEDIDO=EstadoName).first()).ID_ESTADO
            SQLAlchemyBD.session.commit()
            return True
        except Exception as e:
            print(f"Error en la linea {sys.exc_info()[-1].tb_lineno} de UpdatePedidosStatusCliente: {e}")
            return False

    @classmethod
    def ObtenerProductosPedidos(cls, NegocioId, PedidoId):
        try:
            PedidosProductos = SQLAlchemyBD.session.query(
                PedidosD.ID,
                PedidosD.ID_PRODUCTO,
                PedidosD.CANTIDAD,
                PedidosD.PRECIO,
                PedidosD.TOTAL,
                (PedidosD.OBSERVACIONES).label('OBSERVACIONES_PEDIDOD'),
                NegociosProductos.PRODUCTO,
                NegociosProductos.DESCRIPCION,
                NegociosProductos.FOTO,
                #NegociosProductos.PRECIO,
                NegociosProductos.ACTIVO,
                (PedidosD.CANTIDAD * NegociosProductos.PRECIO).label('TOTAL_PRECIO_PRODUCTOS')
            ).join(NegociosProductos, PedidosD.ID_PRODUCTO == NegociosProductos.ID_PRODUCTO)\
             .join(PedidosM, PedidosD.ID_PEDIDO == PedidosM.ID_PEDIDO)\
             .filter(PedidosM.ID_NEGOCIO == NegocioId, PedidosD.ID_PEDIDO == PedidoId).all()

            TotalInformationPedido = SQLAlchemyBD.session.query(
                cls.ID_PEDIDO,
                cls.ID_VISITANTE,
                cls.ID_NEGOCIO,
                cls.FECHA_REGISTRO,
                cls.ID_ESTADO,
                PedidosEstados.ESTADO_PEDIDO,
                cls.VALOR,
                cls.LATITUD,
                cls.LONGITUD,
                cls.TOTAL,
                cls.DIRECCION,
                cls.PAGADO,
                cls.ID_FPAGO,
                FormasPago.FORMA_PAGO,
                cls.OBSERVACIONES,
                cls.COMPROBANTE,
                Visitantes.ID_VISITANTE,
                Visitantes.CELULAR,
                Visitantes.NOMBRE,
                Visitantes.EMAIL
            ).join(Visitantes, cls.ID_VISITANTE == Visitantes.ID_VISITANTE)\
            .join(PedidosEstados, cls.ID_ESTADO == PedidosEstados.ID_ESTADO)\
            .join(FormasPago, cls.ID_FPAGO == FormasPago.ID_FPAGO)\
            .filter(cls.ID_NEGOCIO == NegocioId, cls.ID_PEDIDO == PedidoId).all()

            TotalInformationPedidoDict = ConvertToDict(TotalInformationPedido)
            PedidosProductosDict = ConvertToDict(PedidosProductos)

            return {
                "InformationPedido": TotalInformationPedidoDict,
                "InformationProductos": PedidosProductosDict
            }
        except Exception as e:
            print(f"Error en la linea {sys.exc_info()[-1].tb_lineno} de ObtenerProductosPedidos: {e}")
            return False
