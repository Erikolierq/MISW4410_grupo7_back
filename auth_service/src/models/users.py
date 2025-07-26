from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user_security(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)  # Email o nombre de usuario
    nombre = db.Column(db.String(50))
    contrasena = db.Column(db.String(150), nullable=False)  # Debe contener hash
    rol = db.Column(db.String(50))
