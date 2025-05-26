from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from App.controllers.UsuarioController import UsuarioController
from App.functions import *
from flask_login import login_required, current_user
from App.extensions import LoginAppicalaManager
from App.models.AuthUser import AuthUser

LoginAppicalaBp = Blueprint("LoginAppicala", __name__)

@LoginAppicalaBp.route("/LoginAppicala", methods=["GET"])
def LoginAppicala():
    if current_user.is_authenticated:
        return redirect(url_for("LoginAppicala.ValidatedDestinationAccess"))
    return render_template("LoginApp.html")

@LoginAppicalaBp.route("/InicioAppicala", methods=["GET"])
@login_required
@RequiredAccesoDefined(["Administrador", "Cliente"])
def InicioAppicala():
    return render_template("index.html")

@LoginAppicalaBp.route("/ValidarLoginAppicala", methods=["POST"])
def ValidarLoginAppicala():
    ValidarDataLoginAppicala = request.form
    if not ValidarDataLoginAppicala:
        return jsonify({"Message": "", "Amount": 0, "Information": ""}), 400
    UserNameLoginAppicala  = QuitarCarecterSQL(ValidarDataLoginAppicala.get("UserNameLoginAppicala"))
    PasswordLoginAppicala  = QuitarCarecterSQL(ValidarDataLoginAppicala.get("PasswordLoginAppicala"))
    ControllerLoginAppicala, StatusLoginAppicala = UsuarioController.ValidarLoginAppicala(UserNameLoginAppicala, PasswordLoginAppicala, "Cliente")
    return jsonify(ControllerLoginAppicala), StatusLoginAppicala

@LoginAppicalaBp.route("/Logout", methods=["GET"])
def Logout():
    if current_user.is_authenticated:
        UsuarioController.LogoutAppicala()
    return redirect(url_for("LoginAppicala.LoginAppicala"))

@LoginAppicalaBp.route("/ValidatedDestinationAccess", methods=["GET"])
@login_required
@RequiredAccesoDefined(["Administrador", "Cliente"])
def ValidatedDestinationAccess():
    if current_user.is_authenticated:
        if current_user.tipo == "Administrador":
            return redirect(url_for("LoginAppicala.InicioAppicala"))
        elif current_user.tipo == "Cliente":
            return redirect(url_for("LoginAppicala.InicioAppicala"))
    return redirect(url_for("LoginAppicala.Logout"))

@LoginAppicalaManager.user_loader
def load_user(UserData):
    try:
        user_id, nombre, tipo, foto = UserData
        user_data = UsuarioController.LoadUserAppicala(int(user_id), tipo)
        if user_data:
            return AuthUser(user_data.ID_USUARIO, user_data.NOMBRE, tipo, foto)
            #return AuthUser(user_data.ID_USUARIO, user_data.NOMBRE, tipo)
        return None
    except:
        return None






