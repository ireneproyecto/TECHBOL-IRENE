from flask import Blueprint

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/')
def listar():
    return "Lista de pedidos - Funciona ✅"

@pedidos_bp.route('/nuevo')
def nuevo():
    return "Formulario para crear nuevo pedido"