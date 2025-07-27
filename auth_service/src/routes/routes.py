from flask import Blueprint, request, jsonify
from src.services.auth_service import AuthService
from flask_jwt_extended import decode_token
from jwt.exceptions import ExpiredSignatureError


auth_bp = Blueprint('auth', __name__)



@auth_bp.route("/ping", methods=["GET"])
def health_check():
    return 'pong', 200


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = AuthService.login(data)
    if token:
        return jsonify({
            "msg": "Login exitoso",
            "access_token": token
        }), 200
    else:
        return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401


@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    usuario = AuthService.signup(data)
    if usuario:
        return jsonify({
            "msg": "Usuario creado exitosamente",
            "usuario": usuario.usuario,
            "rol": usuario.rol
        }), 201
    else:
        return jsonify({"msg": "El usuario ya existe"}), 409


@auth_bp.route('/verify-token', methods=['POST'])
def verify_token():
    data = request.get_json()
    token = data.get("token")

    if not token:
        return jsonify({"msg": "Token requerido"}), 400

    try:
        decoded = decode_token(token)
        user_id = decoded.get("sub")  # Es un string
        rol = decoded.get("rol")      # Viene de additional_claims

        if not user_id or not rol:
            return jsonify({"msg": "Estructura del token inválida"}), 401

        return jsonify({
            "msg": "Token válido",
            "identity": {
                "id": user_id,
                "rol": rol
            }
        }), 200

    except ExpiredSignatureError:
        return jsonify({"msg": "Token expirado"}), 401
    except Exception as e:
        return jsonify({"msg": "Token inválido", "error": str(e)}), 401

