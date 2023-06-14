from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from backend.models import *
from django.db import connection
from http import HTTPStatus

class DAORegistro :
    def get_user (id) :
        try :
            return User.objects.get(id = id)
        except :
            raise None
    
    def post_user (username, password, nombre, apellido) :
        try :
            reg_user = User(
                username = username,
                email = username,
                password = make_password(password),
                first_name = nombre,
                last_name = apellido,
                is_superuser = False
            )
            reg_user.save()
        except Exception as e :
            print(f"Error desconocido: {str(e)}")
            return False
        return True