from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Cliente

clientes_bp = Blueprint('clientes', __name__)

# LISTAR clientes
@clientes_bp.route('/')
def listar():
    clientes = Cliente.query.all()
    return render_template('clientes/listar.html', clientes=clientes)

# CREAR cliente (mostrar formulario)
@clientes_bp.route('/nuevo', methods=['GET'])
def nuevo():
    return render_template('clientes/nuevo.html')

# GUARDAR cliente
@clientes_bp.route('/crear', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    
    cliente = Cliente(nombre=nombre, telefono=telefono)
    db.session.add(cliente)
    db.session.commit()
    
    return redirect(url_for('clientes.listar'))

# EDITAR cliente
@clientes_bp.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template('clientes/editar.html', cliente=cliente)

# ACTUALIZAR cliente
@clientes_bp.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    cliente = Cliente.query.get_or_404(id)
    cliente.nombre = request.form['nombre']
    cliente.telefono = request.form['telefono']
    
    db.session.commit()
    return redirect(url_for('clientes.listar'))

# ELIMINAR cliente
@clientes_bp.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.listar'))