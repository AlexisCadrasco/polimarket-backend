from flask import Flask
from config import Config
from extensions import db   # <- ahora cargamos db desde extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Importar Blueprint DESPUÉS de inicializar db
    from rrhh.controllers import rrhh_bp
    app.register_blueprint(rrhh_bp, url_prefix="/rrhh")

    with app.app_context():
        from rrhh.models import Empleado, Vendedor, AdministradorRRHH
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
