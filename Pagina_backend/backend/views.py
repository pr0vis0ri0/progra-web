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
        token['es_superusuario'] = user.is_superuser
        print(type(token))
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegistroUsuarioDetail(APIView) :
    serializer_class = RegistroUserSerializer

    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if (serializer.is_valid()):
                data = serializer.data
                if DAOUsuario.post_user(*data.values()):
                    return JSONResponse('Usuario creado.')
                else :
                    return JSONResponse('El usuario no fue creado.')
            else :
                return JSONResponse({ 'errores' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class LoginUsuarioDetail(APIView):
    print("")