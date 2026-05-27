from flask import Blueprint

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/')
def listar():
    return "Lista de productos - Funciona ✅"

@productos_bp.route('/nuevo')
def nuevo():
    return "Formulario para crear nuevo producto"