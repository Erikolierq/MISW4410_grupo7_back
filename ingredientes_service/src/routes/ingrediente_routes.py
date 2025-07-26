from flask import Blueprint, request, jsonify
from src.services.ingredientes_service import IngredienteService
from src.utils.token_validator import require_jwt

ingrediente_bp = Blueprint('ingrediente', __name__)

@ingrediente_bp.route("/ping", methods=["GET"])
def health_check():
    return 'pong', 200


@ingrediente_bp.route('/all', methods=['GET'])
@require_jwt
def listar_ingredientes():
    return jsonify(IngredienteService.listar_todos())



@ingrediente_bp.route('/<int:id_ingrediente>', methods=['GET'])
@require_jwt
def obtener_ingrediente(id_ingrediente):
    ingrediente = IngredienteService.obtener_por_id(id_ingrediente)
    if ingrediente:
        return jsonify(ingrediente)
    return jsonify({"error": "Ingrediente no encontrado"}), 404



@ingrediente_bp.route('/restaurante/<int:id_restaurante>', methods=['GET'])
@require_jwt
def listar_por_restaurante(id_restaurante):
    return jsonify(IngredienteService.listar_por_restaurante(id_restaurante))



@ingrediente_bp.route('/create', methods=['POST'])
@require_jwt
def crear_ingrediente():
    data = request.get_json()
    try:
        nuevo = IngredienteService.crear(data)
        return jsonify(nuevo), 201
    except KeyError as e:
        return jsonify({"error": f"Campo requerido faltante: {e}"}), 400

@ingrediente_bp.route('/<int:id_ingrediente>', methods=['PUT'])
@require_jwt
def actualizar_ingrediente(id_ingrediente):
    data = request.get_json()
    actualizado = IngredienteService.actualizar(id_ingrediente, data)
    if actualizado:
        return jsonify(actualizado)
    return jsonify({"error": "Ingrediente no encontrado"}), 404

@ingrediente_bp.route('/<int:id_ingrediente>', methods=['DELETE'])
@require_jwt
def eliminar_ingrediente(id_ingrediente):
    eliminado = IngredienteService.eliminar(id_ingrediente)
    if eliminado:
        return '', 204
    return jsonify({"error": "Ingrediente no encontrado"}), 404
