from rrhh.dtos import EmpleadoDTO, VendedorDTO
from rrhh.models import Vendedor, AdministradorRRHH

class RRHHService:

    def __init__(self, repository):
        self.repository = repository

    def autorizar_vendedor(self, id_vendedor):
        emp = self.repository.buscar_empleado(id_vendedor)
        if not emp or not isinstance(emp, Vendedor):
            return False
        
        emp.estado_autorizacion = True
        self.repository.guardar_empleado(emp)
        return True

    def obtener_empleado(self, id):
        emp = self.repository.buscar_empleado(id)
        if not emp:
            return None
        return EmpleadoDTO(emp.id, emp.nombre, emp.apellido, emp.email)

    def obtener_info_vendedor(self, id):
        emp = self.repository.buscar_empleado(id)
        if not emp:
            return None
        return VendedorDTO(emp.id, emp.nombre, emp.codigo_vendedor, emp.estado_autorizacion)

    def crear_administrador(self, data):
        admin = AdministradorRRHH(
            nombre=data["nombre"],
            apellido=data["apellido"],
            documento=data["documento"],
            email=data["email"],
            cargo=data["cargo"]
        )
        self.repository.guardar_empleado(admin)
        return admin
