from App.models.UsuarioModel import Usuario
from App.models.NegociosModel import Negocios
from App.models.AuthUser import AuthUser
from flask_login import login_user, logout_user
from flask import session

class UsuarioController:

    @staticmethod
    def ValidarLoginAppicala(UserEmailLoginAppicala, PasswordLoginAppicala, TipoLogueo):
        if TipoLogueo == "Administrador":
            UsuarioValidated = Usuario.GetUserByEmail(UserEmailLoginAppicala)
            if not UsuarioValidated:
                return {"Message": "Exito", "Amount": 0, "Information": ""}, 400
            if UsuarioValidated.EMAIL == UserEmailLoginAppicala:
                if UsuarioValidated.CLAVE == PasswordLoginAppicala:
                    AuthUserModel = AuthUser(id=UsuarioValidated.ID_USUARIO, nombre=UsuarioValidated.NOMBRE, tipo="Administrador", foto="")
                    login_user(AuthUserModel, remember=True)
                    return {"Message": "Exito", "Amount": 1, "Information": "Autenticado"}, 200
                else:
                    return {"Message": "Exito", "Amount": 0, "Information": "Credenciales Incorrectas"}, 401
            else:
                return {"Message": "Exito", "Amount": 0, "Information": "Credenciales Incorrectas"}, 401
        elif TipoLogueo == "Cliente":
            try:
                UsuarioValidated = Negocios.GetUserByUser(UserEmailLoginAppicala)
                if not UsuarioValidated:
                    return {"Message": "Exito", "Amount": 0, "Information": "Credenciales Incorrectas"}, 401
                if UsuarioValidated.USUARIO == UserEmailLoginAppicala:
                    if UsuarioValidated.CLAVE == PasswordLoginAppicala:
                        AuthUserModel = AuthUser(id=UsuarioValidated.ID_USUARIO, nombre=UsuarioValidated.NOMBRE, tipo="Cliente", foto=UsuarioValidated.FOTO)
                        login_user(AuthUserModel, remember=True)
                        return {"Message": "Exito", "Amount": 1, "Information": "Autenticado"}, 200
                    else:
                        return {"Message": "Exito", "Amount": 0, "Information": "Credenciales Incorrectas"}, 401
                else:
                    return {"Message": "Exito", "Amount": 0, "Information": "Credenciales Incorrectas"}, 401
            except Exception as e:
                return {"Message": "Exito", "Amount": 0, "Information": f"Error BD: {e}"}, 400
        else:
            return {"Message": "Exito", "Amount": 0, "Information": "Credenciales Incorrectas"}, 401

    @staticmethod
    def LoadUserAppicala(user_id, TipoUsuario):
        if TipoUsuario == "Administrador":
            UsuarioValidated = Usuario.query.get(int(user_id))
        elif TipoUsuario == "Cliente":
            UsuarioValidated = Negocios.query.get(int(user_id))
        else:
            UsuarioValidated = None
        return UsuarioValidated

    @staticmethod
    def LogoutAppicala():
        logout_user()
        session.clear()
        return {"Message": "Exito", "Amount": 0, "Information": "Sesión Cerrada"}, 200


