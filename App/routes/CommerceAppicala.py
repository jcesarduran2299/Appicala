from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from App.functions import *
from flask_login import login_required, current_user
from App.controllers.CommerceAppicalaController import CommerceAppicalaController

CommerceAppicalaBp = Blueprint("CommerceAppicala", __name__)

@CommerceAppicalaBp.route("/ListarCuentaPedidosStatusCliente", methods=["POST"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarCuentaPedidosStatusCliente():
    ResponseListarPedidosStatusCliente = CommerceAppicalaController.ListarCuentaPedidosStatusCliente()
    if ResponseListarPedidosStatusCliente == False:
        return jsonify({"Message": "Exito", "Amount": 0, "Information": []}), 400
    else:
        return jsonify({"Message": "Exito", "Amount": 1, "Information": ResponseListarPedidosStatusCliente}), 200

@CommerceAppicalaBp.route("/ListarPedidosStatusCliente", methods=["GET"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarPedidosStatusCliente():
    return render_template("ListarPedidosStatusCliente.html")

@CommerceAppicalaBp.route("/ListarPedidosStatusClienteInformationEspera", methods=["POST"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarPedidosStatusClienteInformationEspera():
    ResponseListarPedidosStatusCliente = CommerceAppicalaController.ListarPedidosStatusCliente("EN ESPERA")
    return jsonify({"data": ResponseListarPedidosStatusCliente}), 200

@CommerceAppicalaBp.route("/ListarPedidosStatusClienteInformationPreparacion", methods=["POST"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarPedidosStatusClienteInformationPreparacion():
    ResponseListarPedidosStatusCliente = CommerceAppicalaController.ListarPedidosStatusCliente("EN PREPARACION")
    return jsonify({"data": ResponseListarPedidosStatusCliente}), 200

@CommerceAppicalaBp.route("/ListarPedidosStatusClienteInformationCamino", methods=["POST"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarPedidosStatusClienteInformationCamino():
    ResponseListarPedidosStatusCliente = CommerceAppicalaController.ListarPedidosStatusCliente("EN CAMINO")
    return jsonify({"data": ResponseListarPedidosStatusCliente}), 200

@CommerceAppicalaBp.route("/ListarPedidosStatusClienteInformationEntregado", methods=["POST"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarPedidosStatusClienteInformationEntregado():
    ResponseListarPedidosStatusCliente = CommerceAppicalaController.ListarPedidosStatusCliente("ENTREGADO")
    return jsonify({"data": ResponseListarPedidosStatusCliente}), 200

@CommerceAppicalaBp.route("/UpdatePedidosStatusClienteInformation", methods=["POST"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def UpdatePedidosStatusClienteInformation():
    UpdatePedidosStatusClienteInformation = request.form
    if not UpdatePedidosStatusClienteInformation:
        return jsonify({"Message": "Exito", "Amount": 0, "Information": ""}), 400
    IdPedidoClient = QuitarCarecterSQL(UpdatePedidosStatusClienteInformation.get("IdPedidoClient"))
    StatusPedidoClient = QuitarCarecterSQL(UpdatePedidosStatusClienteInformation.get("StatusPedidoClient"))
    ControllerCommerceAppicala, StatusCommerceAppicala = CommerceAppicalaController.UpdatePedidosStatusClienteInformation(IdPedidoClient, StatusPedidoClient)
    return jsonify(ControllerCommerceAppicala), StatusCommerceAppicala

@CommerceAppicalaBp.route("/ListarProductosCliente", methods=["GET"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarProductosCliente():
    return render_template("ListarProductosStatusCliente.html")

@CommerceAppicalaBp.route("/ListarPedidosProductosCliente/", methods=["GET"])
@CommerceAppicalaBp.route("/ListarPedidosProductosCliente/<int:NumeroPedido>/NumeroPedido", methods=["GET"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ListarPedidosProductosCliente(NumeroPedido = None):
    print("NumeroPedido")
    print(NumeroPedido)
    if NumeroPedido:
        ListarPedidosProductosCliente, StatusPedidosProductosCliente = CommerceAppicalaController.ListarPedidosProductosCliente(NumeroPedido)
        ListarPedidosProductosClienteSerializable = json.dumps(ListarPedidosProductosCliente, default=custom_serializer, ensure_ascii=False)
        ListarPedidosProductosClienteObjeto = json.loads(ListarPedidosProductosClienteSerializable)
        return render_template("ListarPedidosProductosCliente.html",
                               ListarPedidosProductosCliente=ListarPedidosProductosClienteObjeto,
                               StatusPedidosProductosCliente=StatusPedidosProductosCliente)
    else:
        return redirect(url_for("CommerceAppicala.ListarPedidosStatusCliente"))



@CommerceAppicalaBp.route("/ModificarInformacionEmpresa/", methods=["GET"])
@login_required
@RequiredAccesoDefined(["Administador", "Cliente"])
def ModificarInformacionEmpresa():
    return render_template("ModificarInformacionEmpresa.html")