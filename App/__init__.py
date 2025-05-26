from flask import Flask, render_template
from App.extensions import InitSQLAlchemyBD, InitLoginManager
from App.routes.Default import DefaultAppicalaBp
from App.routes.LoginAppicala import LoginAppicalaBp
from App.routes.CommerceAppicala import CommerceAppicalaBp
from App.extensions import SQLAlchemyBD

def CreateAppFlask():
    AppFlask = Flask(__name__)

    # Configuración de la app
    AppFlask.config.from_object("App.config.Config")
    InitSQLAlchemyBD(AppFlask)
    InitLoginManager(AppFlask)

    @AppFlask.errorhandler(404)
    def PaginaNoEncontrada(error):
        return render_template("404.html"), 404

    # Registrar Blueprints
    AppFlask.register_blueprint(DefaultAppicalaBp)
    AppFlask.register_blueprint(LoginAppicalaBp)
    AppFlask.register_blueprint(CommerceAppicalaBp)

    return AppFlask





