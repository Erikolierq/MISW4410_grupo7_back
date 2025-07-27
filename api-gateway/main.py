from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
# URLs y prefijos reales
SERVICES = {
    'auth': "http://auth-service:3001",
    'ingrediente': "http://ingrediente-service:3002",
    'receta': "http://receta-service:3003",
    'menu': "http://menu-service:3004",
    'restaurante': "http://restaurante-service:3005"
}

# Prefijos internos de ruta para cada servicio
SERVICE_PREFIXES = {
    'auth': 'auth',
    'ingrediente' :'ingrediente',
    'receta' : 'receta',
    'menu' : 'menu',
    'restaurante' : 'restaurante'

}

@app.route('/<service>/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def proxy(service, path):
    if service not in SERVICES:
        return jsonify({"error": "Servicio no reconocido"}), 404

    service_url = SERVICES[service]
    prefix = SERVICE_PREFIXES.get(service, '')
    query_string = request.query_string.decode()

    if prefix:
        full_path = f"{service_url}/{prefix}/{path}"
    else:
        full_path = f"{service_url}/{path}"

    url = f"{full_path}?{query_string}" if query_string else full_path

    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for key, value in request.headers if key.lower() != 'host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        return (response.content, response.status_code, response.headers.items())
    except requests.RequestException as e:
        return jsonify({"error": "Servicio no disponible", "details": str(e)}), 503


@app.route('/')
def home():
    return jsonify({"message": "API Gateway activo y redirigiendo a microservicios"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
