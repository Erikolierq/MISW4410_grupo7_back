from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)

class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'
    id = db.Column(db.Integer, primary_key=True)
class Receta(db.Model):
    __tablename__ = 'receta'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    duracion = db.Column(db.Numeric, nullable=False)
    preparacion = db.Column(db.Text, nullable=False)
    porcion = db.Column(db.String(50))
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    menu = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=True)
    ingredientes = db.relationship('RecetaIngrediente', cascade='all, delete, delete-orphan')

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
    
class RecetaIngrediente(db.Model):
    __tablename__ = 'receta_ingrediente'

    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Numeric, nullable=False)
    ingrediente = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), nullable=False)
    receta = db.Column(db.Integer, db.ForeignKey('receta.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "cantidad": float(self.cantidad),
            "ingrediente": self.ingrediente,
            "receta": self.receta
        }
