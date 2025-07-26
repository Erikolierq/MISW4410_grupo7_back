from flask import Blueprint, request, jsonify
from src.services.receta_service import RecetaService
from src.utils.token_validator import require_jwt

receta_bp = Blueprint('receta', __name__)



@receta_bp.route("/ping", methods=["GET"])
def health_check():
    return 'pong', 200

@receta_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
@require_jwt
def listar_recetas(id_usuario):
    return jsonify(RecetaService.listar_por_usuario(id_usuario))

@receta_bp.route('/<int:id_receta>', methods=['GET'])
@require_jwt
def obtener(id_receta):
    receta = RecetaService.obtener(id_receta)
    if receta:
        return jsonify(receta)
    return jsonify({"error": "No encontrada"}), 404

@receta_bp.route('/create', methods=['POST'])
@require_jwt
def crear():
    data = request.get_json()
    return jsonify(RecetaService.crear(data)), 201

@receta_bp.route('/<int:id_receta>', methods=['PUT'])
@require_jwt
def actualizar(id_receta):
    data = request.get_json()
    receta = RecetaService.actualizar(id_receta, data)
    if receta:
        return jsonify(receta)
    return jsonify({"error": "No encontrada"}), 404

@receta_bp.route('/<int:id_receta>', methods=['DELETE'])
@require_jwt
def eliminar(id_receta):
    if RecetaService.eliminar(id_receta):
        return '', 204
    return jsonify({"error": "No encontrada"}), 404
