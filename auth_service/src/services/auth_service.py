from src.models.users import db, user_security
from flask_jwt_extended import create_access_token

class AuthService:

    @staticmethod
    def login(data):
        usuario = user_security.query.filter_by(usuario=data.get("usuario")).first()
        if not usuario or usuario.contrasena != data.get("contrasena"):
            return None
        return create_access_token(
            identity=str(usuario.id),  
            additional_claims={"rol": usuario.rol}
        )

    @staticmethod
    def signup(data):
        if user_security.query.filter_by(usuario=data.get("usuario")).first():
            return None

        nuevo_usuario = user_security(
            usuario=data.get("usuario"),
            nombre=data.get("nombre"),
            contrasena=data.get("contrasena"),  
            rol=data.get("rol", "usuario")      
        )

        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario
