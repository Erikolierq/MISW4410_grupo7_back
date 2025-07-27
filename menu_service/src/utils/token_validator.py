from functools import wraps
from flask import request, jsonify, g
import requests

GATEWAY_AUTH_URL = 'http://api-gateway:3000/auth/verify-token'

def require_jwt(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"msg": "Token no proporcionado"}), 401

        token = auth_header.split(" ")[1]
        try:
            response = requests.post(GATEWAY_AUTH_URL, json={"token": token})
            if response.status_code != 200:
                return jsonify({"msg": "Token inválido"}), 401
            g.identity = response.json()["identity"]
        except Exception as e:
            return jsonify({"msg": f"Error al verificar token: {str(e)}"}), 500

        return f(*args, **kwargs)
    return decorated
