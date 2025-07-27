from flask import Blueprint, request, jsonify
from src.services.menu_service import MenuService
from src.utils.token_validator import require_jwt  

menu_bp = Blueprint('menu', __name__)

@menu_bp.route("/ping", methods=["GET"])
def health_check():
    return "pong", 200

@menu_bp.route("/all", methods=["GET"])
@require_jwt
def listar_menus():
    return jsonify(MenuService.listar_todos())

@menu_bp.route("/<int:id_menu>", methods=["GET"])
@require_jwt
def obtener_menu(id_menu):
    menu = MenuService.obtener(id_menu)
    if menu:
        return jsonify(menu)
    return jsonify({"error": "Menu no encontrado"}), 404

@menu_bp.route("/create", methods=["POST"])
@require_jwt
def crear_menu():
    data = request.get_json()
    try:
        nuevo = MenuService.crear(data)
        return jsonify(nuevo), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@menu_bp.route("/<int:id_menu>", methods=["PUT"])
@require_jwt
def actualizar_menu(id_menu):
    data = request.get_json()
    actualizado = MenuService.actualizar(id_menu, data)
    if actualizado:
        return jsonify(actualizado)
    return jsonify({"error": "Menu no encontrado"}), 404

@menu_bp.route("/<int:id_menu>", methods=["DELETE"])
@require_jwt
def eliminar_menu(id_menu):
    eliminado = MenuService.eliminar(id_menu)
    if eliminado:
        return "", 204
    return jsonify({"error": "Menu no encontrado"}), 404


