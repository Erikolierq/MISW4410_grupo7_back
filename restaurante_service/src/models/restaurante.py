from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurante(db.Model):
    __tablename__ = 'restaurante'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    direccion = db.Column(db.String(256))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(128))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "correo": self.correo
        }
