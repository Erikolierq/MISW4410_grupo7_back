from flask import Blueprint, request, jsonify
from src.services.restaurante_service import RestauranteService
from src.utils.token_validator import require_jwt
restaurante_bp = Blueprint('restaurante', __name__)

@restaurante_bp.route("/ping", methods=["GET"])
def health_check():
    return "pong", 200

@restaurante_bp.route("/all", methods=["GET"])
@require_jwt
def listar_restaurantes():
    return jsonify(RestauranteService.listar_todos())

@restaurante_bp.route("/<int:id_restaurante>", methods=["GET"])
@require_jwt
def obtener_restaurante(id_restaurante):
    restaurante = RestauranteService.obtener_por_id(id_restaurante)
    if restaurante:
        return jsonify(restaurante)
    return jsonify({"error": "Restaurante no encontrado"}), 404

@restaurante_bp.route("/create", methods=["POST"])
@require_jwt
def crear_restaurante():
    data = request.get_json()
    return jsonify(RestauranteService.crear(data)), 201

@restaurante_bp.route("/<int:id_restaurante>", methods=["PUT"])
@require_jwt
def actualizar_restaurante(id_restaurante):
    data = request.get_json()
    restaurante = RestauranteService.actualizar(id_restaurante, data)
    if restaurante:
        return jsonify(restaurante)
    return jsonify({"error": "Restaurante no encontrado"}), 404

@restaurante_bp.route("/<int:id_restaurante>", methods=["DELETE"])
@require_jwt
def eliminar_restaurante(id_restaurante):
    if RestauranteService.eliminar(id_restaurante):
        return '', 204
    return jsonify({"error": "Restaurante no encontrado"}), 404
