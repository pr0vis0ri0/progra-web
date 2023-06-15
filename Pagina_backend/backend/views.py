from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from backend.DAO.DAOPropiedad import DAOPropiedad
from backend.DAO.DAORegistro import DAORegistro
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

class RegistroUsuarioDetail(APIView) :
    serializer_class = UserSerializer

    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if (serializer.is_valid()):
                data = serializer.data
                if DAORegistro.post_user(*data.values()):
                    return JSONResponse('Usuario creado.')
                else :
                    return JSONResponse('El usuario no fue creado.')
            else :
                return JSONResponse({ 'errores' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class PropiedadList(APIView):
    def get(self, request):
        registros = DAOPropiedad.get_detalle_propiedades()
        serializer = DetallePropiedadesSerializer(registros, many = True)
        return JSONResponse(serializer.data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(super().validate(attrs))
        refresh = self.get_token(self.user)
        data['id_usuario'] = self.user.id
        data['correo'] = self.user.email
        data['es_superusuario'] = self.user.is_superuser       
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer