from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from backend.models import *
from django.db import connection
from http import HTTPStatus
from backend.jsonresponse import JSONResponse

class DAOUsuario:
    def get_auth_user (id_user) :
        try :
            return User.objects.get(id = id_user)
        except :
            raise None
    
    def get_usuario (id):
        try :
            return Usuario.objects.get(id_usuario = id)
        except Usuario.DoesNotExist:
            raise None
        
    def conseguir_perfil (id_usuario) :
        try :
            return PerfilesUsuario.objects.get(id_usuario = id_usuario)
        except :
            raise None
        
    def registrar_usuario (r_user, r_password, r_email, r_nombre, r_apellido) :
        perfil = DAOUsuario.get_perfil(2)
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
                registro_usuario.auth_user_id = registro_auth_user
                registro_usuario.save()

                perfil_usuario = PerfilesUsuario()
                perfil_usuario.id_perfil = perfil
                perfil_usuario.id_usuario = registro_usuario
                perfil_usuario.save()
            except Exception as e :
                print(f"Error desconocido: {str(e)}")
                return False
            return True
        else :
            return False

    def validar_usuario (p_user, p_password):
        username = p_user
        password = p_password
        user = authenticate(username=username, password=password)
        if user is not None:
            return True
        else:
            return False
        
    def devolver_usuario_perfil (p_user):
        try :
            auth_user = User.objects.get(id = p_user)
            usuario = Usuario.objects.get(auth_user_id = auth_user.id)
            perfil = PerfilesUsuario.objects.get(id_usuario = usuario.id_usuario)
            return {
                'id_usuario' : perfil.id_usuario.id_usuario,
                'id_perfil' : perfil.id_perfil.id_perfil,
            }
        except :
            return None
        
    def devolver_data_usuario (id_user):
        try :
            usuario = Usuario.objects.get(id_usuario = id_user)
        except Usuario.DoesNotExist:
            usuario = None
        
        if usuario is not None:
            return {
                'id_usuario' : usuario.id_usuario,
                'primer_nombre' : usuario.primer_nombre,
                'segundo_nombre' : usuario.segundo_nombre,
                'apellido_paterno' : usuario.apellido_paterno,
                'apellido_materno' : usuario.apellido_materno,
                'email' : usuario.email,
                'rut' : usuario.rut,
                'fecha_nacimiento' : usuario.fecha_nacimiento,
            }
        else :
            return 0
    
    def actualizar_data_usuario (id_usuario, p_nombre, s_nombre, a_paterno, a_materno, email, rut, f_nacimiento) :
        with connection.cursor() as cursor :
            cursor.execute(
            """
                UPDATE 
                    MAESTRO_USUARIOS 
                SET 
                    segundo_nombre = %s, 
                    apellido_materno = %s, 
                    email = %s, 
                    rut = %s,
                    fecha_nacimiento = %s 
                WHERE 
                    id_usuario = %s
            """, [s_nombre, a_materno, email, rut, f_nacimiento, id_usuario])
            result = cursor.rowcount

            if result > 0 :
                return 1
            else :
                return 0