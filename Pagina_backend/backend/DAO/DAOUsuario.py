from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from backend.models import *
from django.db import connection
from http import HTTPStatus
from backend.jsonresponse import JSONResponse

class DAOUsuario :
    def get_auth_user (username) :
        try :
            return User.objects.get(username = username)
        except :
            return None

    def get_usuario (id_usuario) :
        try :
            return Usuario.objects.get(id_usuario = id_usuario)
        except :
            return None

    def registrar_usuario (r_user, r_password, r_email, r_nombre, r_apellido) :
        if DAOUsuario.get_auth_user(r_user) is None :
            try :
            
                registro_auth_user = User()
                registro_auth_user.username = r_user
                registro_auth_user.password = make_password(r_password)
                registro_auth_user.save()

                registro_usuario = Usuario()
                registro_usuario.primer_nombre = r_nombre
                registro_usuario.apellido_paterno = r_apellido
                registro_usuario.email = r_email
                registro_usuario.auth_user_id = DAOUsuario.get_auth_user(registro_auth_user.id)
                registro_usuario.save()

            except Exception as e :
                print(f"Error desconocido: {str(e)}")
                return False
            return True
        else :
            return False