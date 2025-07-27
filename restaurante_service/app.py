from flask import Flask
from flask_cors import CORS
from src.models.restaurante import db
from src.routes.restaurante_route import restaurante_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admindb@dbusers:5432/dbuser'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)
app.register_blueprint(restaurante_bp, url_prefix='/restaurante')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3005, debug=True)
