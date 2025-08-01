from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.routes.routes import auth_bp
from src.models.users import db

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'una_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admindb@dbusers:5432/dbuser'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(auth_bp, url_prefix="/auth")

# ✅ Crear tablas si no existen
with app.app_context():
    from src.models.users import (
        user_security, Restaurante, Ingrediente,
        Menu, Receta, MenuReceta, RecetaIngrediente
    )
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
