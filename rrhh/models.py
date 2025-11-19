from extensions import db

class Empleado(db.Model):
    __tablename__ = "empleados"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    documento = db.Column(db.String(50))
    email = db.Column(db.String(120))
    tipo = db.Column(db.String(50))  # empleado, vendedor, admin

    __mapper_args__ = {
        "polymorphic_identity": "empleado",
        "polymorphic_on": tipo
    }


class Vendedor(Empleado):
    __tablename__ = "vendedores"

    id = db.Column(db.Integer, db.ForeignKey("empleados.id"), primary_key=True)
    codigo_vendedor = db.Column(db.String(50))
    estado_autorizacion = db.Column(db.Boolean, default=False)

    __mapper_args__ = {
        "polymorphic_identity": "vendedor",
    }


class AdministradorRRHH(Empleado):
    __tablename__ = "administradores_rrhh"

    id = db.Column(db.Integer, db.ForeignKey("empleados.id"), primary_key=True)
    cargo = db.Column(db.String(100))

    __mapper_args__ = {
        "polymorphic_identity": "administrador_rrhh",
    }
