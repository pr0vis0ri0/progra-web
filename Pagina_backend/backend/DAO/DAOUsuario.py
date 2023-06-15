from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from backend.models import *
from django.db import connection
from http import HTTPStatus
from backend.jsonresponse import JSONResponse

class DAOUsuario :
    def get_user (username) :
        try :
            return User.objects.get(username = username)
        except :
            return None
    
    def registro_usuario (username, email, password, nombre, apellido) :
        if DAOUsuario.get_user(username) is None :
            try :
                reg_user = User(
                    username = username,
                    password = make_password(password)
                )
                reg_user.save()
                reg_user.email = email
                reg_user.first_name = nombre
                reg_user.last_name = apellido
                reg_user.save()
            except Exception as e :
                print(f"Error desconocido: {str(e)}")
                return False
            return True
        else :
            return False
    
    def login_usuario (username, password) :
        print("Hola.")