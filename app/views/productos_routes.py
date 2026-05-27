from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Producto

productos_bp = Blueprint('productos', __name__)


@productos_bp.route('/')
def listar():
    productos = Producto.query.all()
    return render_template('productos/listar.html', productos=productos)


@productos_bp.route('/nuevo', methods=['GET'])
def nuevo():
    return render_template('productos/nuevo.html')

@productos_bp.route('/crear', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    stock = int(request.form['stock'])
    
    producto = Producto(nombre=nombre, precio=precio, stock=stock)
    db.session.add(producto)
    db.session.commit()
    
    return redirect(url_for('productos.listar'))


@productos_bp.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    producto = Producto.query.get_or_404(id)
    return render_template('productos/editar.html', producto=producto)


@productos_bp.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    producto = Producto.query.get_or_404(id)
    producto.nombre = request.form['nombre']
    producto.precio = float(request.form['precio'])
    producto.stock = int(request.form['stock'])
    
    db.session.commit()
    return redirect(url_for('productos.listar'))


@productos_bp.route('/eliminar/<int:id>')
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos.listar'))