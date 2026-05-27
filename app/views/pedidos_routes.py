from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Pedido, Cliente, Producto
from datetime import datetime

pedidos_bp = Blueprint('pedidos', __name__)

# LISTAR pedidos
@pedidos_bp.route('/')
def listar():
    pedidos = Pedido.query.all()
    return render_template('pedidos/listar.html', pedidos=pedidos)

# CREAR pedido (mostrar formulario)
@pedidos_bp.route('/nuevo', methods=['GET'])
def nuevo():
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    return render_template('pedidos/nuevo.html', clientes=clientes, productos=productos)

# GUARDAR pedido
@pedidos_bp.route('/crear', methods=['POST'])
def crear():
    cliente_id = int(request.form['cliente_id'])
    producto_id = int(request.form['producto_id'])
    monto = float(request.form['monto'])
    
    pedido = Pedido(
        cliente_id=cliente_id,
        producto_id=producto_id,
        monto=monto,
        fecha=datetime.utcnow()
    )
    db.session.add(pedido)
    db.session.commit()
    
    return redirect(url_for('pedidos.listar'))

# EDITAR pedido
@pedidos_bp.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    pedido = Pedido.query.get_or_404(id)
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    return render_template('pedidos/editar.html', pedido=pedido, clientes=clientes, productos=productos)

# ACTUALIZAR pedido
@pedidos_bp.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    pedido = Pedido.query.get_or_404(id)
    pedido.cliente_id = int(request.form['cliente_id'])
    pedido.producto_id = int(request.form['producto_id'])
    pedido.monto = float(request.form['monto'])
    
    db.session.commit()
    return redirect(url_for('pedidos.listar'))

# ELIMINAR pedido
@pedidos_bp.route('/eliminar/<int:id>')
def eliminar(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('pedidos.listar'))