from flask import Flask
from flask_cors import CORS
from src.models.menu import db
from src.routes.menu_route import menu_bp
from sqlalchemy import inspect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admindb@dbusers:5432/dbuser'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, resources={r"/*": {"origins": "*"}})
db.init_app(app)
app.register_blueprint(menu_bp, url_prefix='/menu')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3004, debug=True)
