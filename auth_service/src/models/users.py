from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user_security(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(50))
    contrasena = db.Column(db.String(150), nullable=False)
    rol = db.Column(db.String(50))

class Restaurante(db.Model):
    __tablename__ = 'restaurante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    direccion = db.Column(db.String(256))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(128))

class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    unidad = db.Column(db.String(128), nullable=False)
    costo = db.Column(db.Numeric, nullable=False)
    calorias = db.Column(db.Numeric, nullable=False)
    sitio = db.Column(db.String(128), nullable=True)
    restaurante = db.Column(db.Integer, db.ForeignKey('restaurante.id'), nullable=False)
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    fechainicio = db.Column(db.String(20))
    fechafinal = db.Column(db.String(20))
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    restaurante = db.Column(db.Integer, db.ForeignKey('restaurante.id'), nullable=False)
    recetas = db.relationship('MenuReceta', cascade='all, delete, delete-orphan')
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

class MenuReceta(db.Model):
    __tablename__ = 'menu_receta'
    id = db.Column(db.Integer, primary_key=True)
    id_menu = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    id_receta = db.Column(db.Integer, db.ForeignKey('receta.id'), nullable=False)
    porcion = db.Column(db.Integer)

class RecetaIngrediente(db.Model):
    __tablename__ = 'receta_ingrediente'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Numeric, nullable=False)
    ingrediente = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), nullable=False)
    receta = db.Column(db.Integer, db.ForeignKey('receta.id'), nullable=False)
