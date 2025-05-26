from flask import jsonify, redirect, url_for
from functools import wraps
from flask_login import current_user
from decimal import Decimal
from datetime import datetime
import json, sys

def RequiredAccesoDefined(AccesosPermitted):
    def decorador(f):
        @wraps(f)
        def funcion_envuelta(*args, **kwargs):
            if current_user.tipo not in AccesosPermitted:
                #return jsonify({"Message": "Acceso Denegado", "Amount": 0, "Information": ""}), 403
                return redirect(url_for("LoginAppicala.LoginAppicala"))
            return f(*args, **kwargs)
        return funcion_envuelta
    return decorador

def QuitarCarecterSQL(value):
    if isinstance(value, str):
        return value.replace("'", "")
    return value

def custom_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, tuple):
        return list(obj)
    return str(obj)

def ConvertirValores(value):
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(value, Decimal):
        return float(value)
    return value

def ConvertToDict(VariableConsult):
    ColumnNamesVariableConsult = VariableConsult[0]._fields if VariableConsult else []
    VariableConsultDict = [
        {key: ConvertirValores(value) for key, value in zip(ColumnNamesVariableConsult, row)}
        for row in VariableConsult
    ]
    return VariableConsultDict

