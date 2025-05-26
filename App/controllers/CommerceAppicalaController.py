from App.models.UsuarioModel import Usuario
from App.models.NegociosModel import Negocios
from App.models.PedidosMModel import PedidosM
from flask_login import login_user, logout_user, current_user
from flask import session, jsonify

class CommerceAppicalaController:
    
    def ListarCuentaPedidosStatusCliente():
        PedidosCountM = PedidosM.ObtenerCuentaPedidosClient(current_user.id)
        if PedidosCountM == False:
            return []
        else:
            ResponseDataListarPedidosStatusCliente = [
                {"ID_ESTADO": item[0], "ESTADO_PEDIDO": item[1], "TOTAL_PEDIDOS": item[2]}
                for item in PedidosCountM
            ]
            return ResponseDataListarPedidosStatusCliente

    def ListarPedidosStatusCliente(StateSearch):
        PedidosMAll = PedidosM.ObtenerPedidosWithDetalle(current_user.id, StateSearch)
        return [{
            "ID": PedidosMItem.ID_PEDIDO,
            "ID_PEDIDO": PedidosMItem.ID_PEDIDO,
            "NOMBRE": PedidosMItem.NOMBRE,
            "EMAIL": PedidosMItem.EMAIL,
            "AVATAR": "",
            "PAGADO": "1" if PedidosMItem.PAGADO else "2",
            "ESTADO": PedidosMItem.ID_ESTADO,
            "TOTAL": PedidosMItem.TOTAL,
            "METODO": PedidosMItem.FORMA_PAGO,
            "FECHA_REGISTRO": str(PedidosMItem.FECHA_REGISTRO),
            "HORA": str(PedidosMItem.FECHA_REGISTRO),
            "NUMERO": PedidosMItem.CELULAR,
            "TOTAL_PRODUCTOS": PedidosMItem.TOTAL_PRODUCTOS,
        } for PedidosMItem in PedidosMAll]

    def UpdatePedidosStatusClienteInformation(IdPedidoClient, StatusPedidoClient):
        UpdatePedido = PedidosM.UpdatePedidosStatusCliente(current_user.id, IdPedidoClient, StatusPedidoClient)
        print("UpdatePedido")
        print(UpdatePedido)
        if UpdatePedido:
            return {"Message": "Exito", "Amount": 1, "Information": "Exitoso"}, 200
        else:
            return {"Message": "Exito", "Amount": 0, "Information": "Error en la BD"}, 400

    def ListarPedidosProductosCliente(IdPedidoClient):
        PedidosProductosM = PedidosM.ObtenerProductosPedidos(current_user.id, IdPedidoClient)
        if PedidosProductosM:
            return {"Message": "Exito", "Amount": 1, "Information": PedidosProductosM}, 200
        else:
            return {"Message": "Exito", "Amount": 0, "Information": "Error en la BD"}, 400


