from src.models.restaurante import db, Restaurante
from sqlalchemy.exc import IntegrityError
from flask import abort
import psycopg2.errors

class RestauranteService:

    @staticmethod
    def listar_todos():
        return [r.to_dict() for r in Restaurante.query.all()]

    @staticmethod
    def obtener_por_id(id_restaurante):
        restaurante = Restaurante.query.get(id_restaurante)
        return restaurante.to_dict() if restaurante else None

    @staticmethod
    def crear(data):
        nuevo = Restaurante(**data)
        db.session.add(nuevo)
        db.session.commit()
        return nuevo.to_dict()

    @staticmethod
    def actualizar(id_restaurante, data):
        restaurante = Restaurante.query.get(id_restaurante)
        if not restaurante:
            return None
        for key, value in data.items():
            setattr(restaurante, key, value)
        db.session.commit()
        return restaurante.to_dict()

    @staticmethod
    def eliminar(id_restaurante):
        restaurante = Restaurante.query.get(id_restaurante)
        if not restaurante:
            return False
        db.session.delete(restaurante)
        db.session.commit()
        return True