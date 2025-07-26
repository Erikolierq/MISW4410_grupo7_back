from src.models.receta import db, Receta

class RecetaService:

    @staticmethod
    def listar_por_usuario(id_usuario):
        return [r.to_dict() for r in Receta.query.filter_by(usuario=id_usuario).all()]

    @staticmethod
    def crear(data):
        nueva = Receta(**data)
        db.session.add(nueva)
        db.session.commit()
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
