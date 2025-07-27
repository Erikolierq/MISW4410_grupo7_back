from src.models.ingrediente import db, Ingrediente

class IngredienteService:

    @staticmethod
    def listar_todos():
        return [i.to_dict() for i in Ingrediente.query.all()]

    @staticmethod
    def obtener_por_id(id_ingrediente):
        ingrediente = Ingrediente.query.get(id_ingrediente)
        return ingrediente.to_dict() if ingrediente else None

    @staticmethod
    def listar_por_restaurante(id_restaurante):
        ingredientes = Ingrediente.query.filter_by(restaurante=id_restaurante).all()
        return [i.to_dict() for i in ingredientes]

    @staticmethod
    def crear(data):
        ingrediente = Ingrediente(
            nombre=data['nombre'],
            unidad=data['unidad'],
            costo=data['costo'],
            calorias=data['calorias'],
            sitio=data.get('sitio'),
            restaurante=data['restaurante']
        )
        db.session.add(ingrediente)
        db.session.commit()
        return ingrediente.to_dict()

    @staticmethod
    def actualizar(id_ingrediente, data):
        ingrediente = Ingrediente.query.get(id_ingrediente)
        if not ingrediente:
            return None
        ingrediente.nombre = data.get('nombre', ingrediente.nombre)
        ingrediente.unidad = data.get('unidad', ingrediente.unidad)
        ingrediente.costo = data.get('costo', ingrediente.costo)
        ingrediente.calorias = data.get('calorias', ingrediente.calorias)
        ingrediente.sitio = data.get('sitio', ingrediente.sitio)
        db.session.commit()
        return ingrediente.to_dict()

    @staticmethod
    def eliminar(id_ingrediente):
        ingrediente = Ingrediente.query.get(id_ingrediente)
        if not ingrediente:
            return False
        db.session.delete(ingrediente)
        db.session.commit()
        return True
