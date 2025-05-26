from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

SQLAlchemyBD = SQLAlchemy()
LoginAppicalaManager = LoginManager()

def InitSQLAlchemyBD(app):
    SQLAlchemyBD.init_app(app)

def InitLoginManager(app):
    LoginAppicalaManager.init_app(app)
    LoginAppicalaManager.login_view = "LoginAppicala.LoginAppicala"




