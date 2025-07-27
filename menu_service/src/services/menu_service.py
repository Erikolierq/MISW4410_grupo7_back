from src.models.menu import db, Menu
from sqlalchemy.exc import IntegrityError
from flask import abort
import psycopg2.errors

class MenuService:

    @staticmethod
    def listar_todos():
        return [menu.to_dict() for menu in Menu.query.all()]

    @staticmethod
    def obtener(id_menu):
        menu = Menu.query.get(id_menu)
        return menu.to_dict() if menu else None

    @staticmethod
    def crear(data):
        nuevo_menu = Menu(
            nombre=data.get("nombre"),
            fechainicio=data.get("fechainicio"),
            fechafinal=data.get("fechafinal"),
            usuario=data.get("usuario"),
            restaurante=data.get("restaurante")
        )
        db.session.add(nuevo_menu)
        db.session.commit()
        return nuevo_menu.to_dict()

    @staticmethod
    def actualizar(id_menu, data):
        menu = Menu.query.get(id_menu)
        if not menu:
            return None
        for key, value in data.items():
            setattr(menu, key, value)
        db.session.commit()
        return menu.to_dict()

    @staticmethod
    def eliminar(id_menu):
        menu = Menu.query.get(id_menu)
        if not menu:
            return False
        db.session.delete(menu)
        db.session.commit()
        return True