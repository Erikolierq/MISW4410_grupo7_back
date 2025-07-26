from src.models.receta import db, Receta
from sqlalchemy.exc import IntegrityError
from flask import abort
import psycopg2.errors
class RecetaService:

    @staticmethod
    def listar_por_usuario(id_usuario):
        return [r.to_dict() for r in Receta.query.filter_by(usuario=id_usuario).all()]

    @staticmethod
    def crear(data):
        nueva = Receta(**data)
        db.session.add(nueva)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()

            # Validar error específico por clave foránea en PostgreSQL
            if isinstance(e.orig, psycopg2.errors.ForeignKeyViolation):
                detalle = str(e.orig)

                if 'usuario' in detalle:
                    abort(400, description=f"Error: El usuario con ID {data.get('usuario')} no existe.")
                elif 'menu' in detalle:
                    abort(400, description=f"Error: El menú con ID {data.get('menu')} no existe.")
            
            # Otros errores de integridad
            abort(400, description="Error de integridad en la base de datos. Verifique los datos enviados.")

        return nueva.to_dict()
    


    @staticmethod
    def obtener(id_receta):
        receta = Receta.query.get(id_receta)
        return receta.to_dict() if receta else None

    @staticmethod
    def actualizar(id_receta, data):
        receta = Receta.query.get(id_receta)
        if not receta:
            return None
        for key, value in data.items():
            setattr(receta, key, value)
        db.session.commit()
        return receta.to_dict()

    @staticmethod
    def eliminar(id_receta):
        receta = Receta.query.get(id_receta)
        if not receta:
            return False
        db.session.delete(receta)
        db.session.commit()
        return True
