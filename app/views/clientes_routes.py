from flask import Blueprint

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/')
def listar():
    return "Lista de clientes - Funciona ✅"

@clientes_bp.route('/nuevo')
def nuevo():
    return "Formulario para crear nuevo cliente"