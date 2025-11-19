class EmpleadoDTO:
    def __init__(self, id, nombre, apellido, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email


class VendedorDTO:
    def __init__(self, id, nombre, codigo_vendedor, estado_autorizacion):
        self.id = id
        self.nombre = nombre
        self.codigo_vendedor = codigo_vendedor
        self.estado_autorizacion = estado_autorizacion
