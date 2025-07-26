from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Receta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    duracion = db.Column(db.Numeric, nullable=False)
    preparacion = db.Column(db.Text, nullable=False)
    porcion = db.Column(db.String(50))
    usuario = db.Column(db.Integer, nullable=False)
    menu = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "duracion": float(self.duracion),
            "preparacion": self.preparacion,
            "porcion": self.porcion,
            "usuario": self.usuario,
            "menu": self.menu
        }
