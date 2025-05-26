from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_login import LoginManager, current_user

DefaultAppicalaBp = Blueprint("DefaultAppicala", __name__)

@DefaultAppicalaBp.route("/", methods=["GET"])
def InicioAppicala():
    return redirect(url_for("LoginAppicala.LoginAppicala"))





