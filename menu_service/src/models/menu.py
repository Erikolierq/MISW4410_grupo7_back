from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo mínimo de usuario para la relación FK
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)

# Modelo mínimo de receta para la relación FK
class Receta(db.Model):
    __tablename__ = 'receta'
    id = db.Column(db.Integer, primary_key=True)

class Restaurante(db.Model):
    __tablename__ = 'restaurante'
    id = db.Column(db.Integer, primary_key=True)

# Modelo de MenuReceta (tabla intermedia)
class MenuReceta(db.Model):
    __tablename__ = 'menu_receta'

    id = db.Column(db.Integer, primary_key=True)
    id_menu = db.Column(db.Integer, db.ForeignKey('menu.id'))
    id_receta = db.Column(db.Integer, db.ForeignKey('receta.id'))
    porcion = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "id_menu": self.id_menu,
            "id_receta": self.id_receta,
            "porcion": self.porcion
        }

# Modelo principal de Menu
class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    fechainicio = db.Column(db.String(20))
    fechafinal = db.Column(db.String(20))
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    restaurante = db.Column(db.Integer, db.ForeignKey('restaurante.id'))
    recetas = db.relationship('MenuReceta', cascade='all, delete, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fechainicio": self.fechainicio,
            "fechafinal": self.fechafinal,
            "usuario": self.usuario,
            "restaurante": self.restaurante,
            "recetas": [r.to_dict() for r in self.recetas]
        }
