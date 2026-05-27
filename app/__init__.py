from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    db.init_app(app)
    migrate.init_app(app, db)
    

    from app import models
    

    from app.views.clientes_routes import clientes_bp
    from app.views.productos_routes import productos_bp
    from app.views.pedidos_routes import pedidos_bp
    
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(pedidos_bp, url_prefix='/pedidos')
    

    @app.route('/')
    def index():
        return 'Bienvenido a TechBol - Sistema de Inventario'
    
    return app