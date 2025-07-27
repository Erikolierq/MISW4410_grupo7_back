from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    unidad = db.Column(db.String(128), nullable=False)
    costo = db.Column(db.Numeric, nullable=False)
    calorias = db.Column(db.Numeric, nullable=False)
    sitio = db.Column(db.String(128), nullable=True)
    restaurante = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "unidad": self.unidad,
            "costo": float(self.costo),
            "calorias": float(self.calorias),
            "sitio": self.sitio,
            "restaurante": self.restaurante
        }
