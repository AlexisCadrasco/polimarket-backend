from flask import Blueprint, jsonify, request
from rrhh.repository import RRHHRepository
from rrhh.services import RRHHService
from rrhh.models import Vendedor, AdministradorRRHH

rrhh_bp = Blueprint("rrhh", __name__)

repo = RRHHRepository()
service = RRHHService(repo)


@rrhh_bp.route("/vendedor/crear", methods=["POST"])
def crear_vendedor():
    data = request.json
    
    vendedor = Vendedor(
        nombre=data["nombre"],
        apellido=data["apellido"],
        documento=data["documento"],
        email=data["email"],
        codigo_vendedor=data["codigo_vendedor"],
        estado_autorizacion=False
    )

    repo.guardar_empleado(vendedor)
    return jsonify({"message": "Vendedor creado"}), 201


@rrhh_bp.route("/vendedor/autorizar/<int:id>", methods=["POST"])
def autorizar(id):
    success = service.autorizar_vendedor(id)
    return jsonify({"autorizado": success})


@rrhh_bp.route("/vendedor/<int:id>", methods=["GET"])
def obtener_info(id):
    dto = service.obtener_info_vendedor(id)
    if not dto:
        return jsonify({"error": "No encontrado"}), 404
    return jsonify(dto.__dict__)


@rrhh_bp.route("/administrador/crear", methods=["POST"])
def crear_administrador():
    data = request.json

    admin = AdministradorRRHH(
        nombre=data["nombre"],
        apellido=data["apellido"],
        documento=data["documento"],
        email=data["email"],
        cargo=data["cargo"],
        tipo="administrador_rrhh"
    )

    repo.guardar_empleado(admin)
    return jsonify({"message": "Administrador RRHH creado"}), 201