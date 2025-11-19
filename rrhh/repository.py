from extensions import db
from rrhh.models import Empleado

class RRHHRepository:

    def buscar_empleado(self, id):
        return Empleado.query.get(id)

    def guardar_empleado(self, empleado):
        db.session.add(empleado)
        db.session.commit()
