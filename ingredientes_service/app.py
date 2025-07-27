from flask import Flask
from flask_cors import CORS
from src.models.ingrediente import db
from src.routes.ingrediente_routes import ingrediente_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admindb@dbusers:5432/dbuser'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)
app.register_blueprint(ingrediente_bp, url_prefix='/ingrediente')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002, debug=True)
