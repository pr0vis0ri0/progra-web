from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from backend.DAO.DAOPropiedad import DAOPropiedad
from backend.DAO.DAOUsuario import DAOUsuario
from .jsonresponse import JSONResponse

class PropiedadDetail(APIView):
    def get(self, request, id_propiedad = None):
        if id_propiedad is not None :
            registro = DAOPropiedad.get_caracteristicas_propiedad(id_propiedad)
            serializer = ViewCaracteristicasSerializer(registro)
            return JSONResponse(serializer.data)
    
class RegistroPropiedadDetail(APIView):
    serializer_class = RegistroPropiedadSerializer
    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid() :
                data = serializer.data
                if DAOPropiedad.post_registrar_propiedad(*data.values()):
                    return JSONResponse('Registro creado.')
                else :
                    return JSONResponse(status.HTTP_400_BAD_REQUEST)
            else :
                return JSONResponse({ 'errores' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido: {str(e)}")
            return False

class FiltroPropiedadDetail(APIView):
    serializer_class = FiltroPropiedadSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            registros = DAOPropiedad.get_propiedades_filtradas(*data.values())
            if isinstance(registros, dict) :
                serializer = DetallePropiedadesSerializer(registros, many = False)
                return JSONResponse(serializer.data)
            elif isinstance(registros, list) :
                serializer = DetallePropiedadesSerializer(registros, many = True)
                return JSONResponse(serializer.data)
            else :
                return JSONResponse({'mensaje-error' : 'No se encontraron registros.', 'status-error' : status.HTTP_404_NOT_FOUND})
        else :
            return JSONResponse({ 'errores' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})

class PropiedadList(APIView):
    def get(self, request):
        registros = DAOPropiedad.get_detalle_propiedades()
        serializer = DetallePropiedadesSerializer(registros, many = True)
        return JSONResponse(serializer.data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        queryset = DAOUsuario.devolver_usuario_perfil(user.id)
        token['id_perfil'] = queryset['id_perfil']
        token['id_usuario'] = queryset['id_usuario']
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegistroUsuario(APIView) :
    serializer_class = RegistroUserSerializer

    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if (serializer.is_valid()):
                data = serializer.data
                if DAOUsuario.registrar_usuario(*data.values()):
                    return JSONResponse('Usuario creado.')
                else :
                    return JSONResponse('El usuario no fue creado, debido a que ese correo ya está siendo utilizado.')
            else :
                return JSONResponse({ 'errores' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class LoginView(APIView):
    serializer_class = LoginUserSerializer
    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                if DAOUsuario.validar_usuario(*data.values()):
                    user_search = User.objects.get(username = data['username'])
                    token_serializer = MyTokenObtainPairSerializer()
                    token = token_serializer.get_token(user_search)
                    access_token = str(token.access_token)
                    refresh_token = str(token)
                    return JSONResponse({
                        'access': access_token,
                        'refresh': refresh_token,
                    })
                else :
                    return JSONResponse({'mensaje-error' : 'Credenciales incorrectas.', 'status-error' : status.HTTP_404_NOT_FOUND})
            else :
                return JSONResponse({ 'errores' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False