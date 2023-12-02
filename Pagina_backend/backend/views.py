from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid() :
                data = serializer.data
                print(data)
                if DAOPropiedad.post_registrar_propiedad(*data.values()):
                    print('aquí no')
                    return JSONResponse('Registro creado.')
                else :
                    print('aquí?')
                    return JSONResponse(status.HTTP_400_BAD_REQUEST)
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        # except BaseException as e :
        #     print(f"Error desconocido: {str(e)}")
        #     return JSONResponse({'mensaje-error': 'Error desconocido'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
                return JSONResponse({'mensaje-error' : 'No se encontraron registros.', 'status' : status.HTTP_404_NOT_FOUND})
        else :
            return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})

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
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
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
                    return JSONResponse({'mensaje-error' : 'Credenciales incorrectas.', 'status' : status.HTTP_404_NOT_FOUND})
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False
        
class PropiedadesPendientes(APIView):
    serializer_class = BasePropiedadesSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registros = DAOPropiedad.get_propiedades_pendientes(data['id_usuario'])
                if isinstance(registros, dict) :
                    serializer = TablasPropiedadesSerializer(registros, many = False)
                    return JSONResponse(serializer.data)
                elif isinstance(registros, list) :
                    serializer = TablasPropiedadesSerializer(registros, many = True)
                    return JSONResponse(serializer.data)
                else :
                    return JSONResponse({'mensaje-error' : 'No se encontraron registros.', 'status' : status.HTTP_404_NOT_FOUND})
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class PropiedadPendienteDetail(APIView):
    serializer_class = DetallePropiedadSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registro = DAOPropiedad.get_caracteristicas_propiedad_pendiente(*data.values())
                serializer = ViewCaracteristicasSerializer(registro, many = False)
                return JSONResponse(serializer.data)
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class PropiedadesValidadas(APIView):
    serializer_class = BasePropiedadesSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registros = DAOPropiedad.get_propiedades_validadas(data['id_usuario'])
                if isinstance(registros, dict) :
                    serializer = TablasPropiedadesSerializer(registros, many = False)
                    return JSONResponse(serializer.data)
                elif isinstance(registros, list) :
                    serializer = TablasPropiedadesSerializer(registros, many = True)
                    return JSONResponse(serializer.data)
                else :
                    return JSONResponse({'mensaje-error' : 'No se encontraron registros.', 'status' : status.HTTP_404_NOT_FOUND})
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

# hazme una clase para mostrar el detalle de la propiedad validada
class PropiedadValidadaDetail(APIView):
    serializer_class = DetallePropiedadSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registro = DAOPropiedad.get_caracteristicas_propiedad_validada(*data.values())
                serializer = ViewCaracteristicasSerializer(registro, many = False)
                return JSONResponse(serializer.data)
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False
        
class AdminPropiedadesPendientes(APIView):
    serializer_class = BasePropiedadesSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registros = DAOPropiedad.get_propiedades_pendientes_administrador(data['id_usuario'])
                if isinstance(registros, dict) :
                    serializer = AdminPropiedadesSerializer(registros, many = False)
                    return JSONResponse(serializer.data)
                elif isinstance(registros, list) :
                    serializer = AdminPropiedadesSerializer(registros, many = True)
                    return JSONResponse(serializer.data)
                elif registros == 5 :
                    return JSONResponse({'mensaje-error' : 'No cuentas con los permisos para ingresar a esta ruta.', 'status' : status.HTTP_401_UNAUTHORIZED})
                else :
                    return JSONResponse({'mensaje-error' : 'No se encontraron registros.', 'status' : status.HTTP_404_NOT_FOUND})
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class AdminPropiedadesBase(APIView):
    serializer_class = BasePropiedadesSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registros = DAOPropiedad.get_propiedades_base_administrador(data['id_usuario'])
                if isinstance(registros, dict) :
                    serializer = AdminPropiedadesSerializer(registros, many = False)
                    return JSONResponse(serializer.data)
                elif isinstance(registros, list) :
                    serializer = AdminPropiedadesSerializer(registros, many = True)
                    return JSONResponse(serializer.data)
                elif registros == 5 :
                    return JSONResponse({'mensaje-error' : 'No cuentas con los permisos para ingresar a esta ruta.', 'status' : status.HTTP_401_UNAUTHORIZED})
                else :
                    return JSONResponse({'mensaje-error' : 'No se encontraron registros.', 'status' : status.HTTP_404_NOT_FOUND})
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class DetallePropiedadAdmin(APIView):
    serializer_class_post = DetallePropiedadSerializer
    serializer_class_put = PutPropiedadSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try :
            serializer = self.serializer_class_post(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registro = DAOPropiedad.get_detalle_propiedad_administrador(*data.values())
                if registro == 0 :
                    return JSONResponse({'mensaje-error' : 'No cuentas con los permisos para ingresar a esta ruta.', 'status' : status.HTTP_401_UNAUTHORIZED})
                serializer = AdminPropiedadesSerializer(registro, many = False)
                return JSONResponse(serializer.data)
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False
    
    def put(self, request):
        try :
            serializer = self.serializer_class_put(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registro = DAOPropiedad.put_propiedad_admin(*data.values())
                if registro == 1 :
                    return JSONResponse({'mensaje-success' : 'Se logró actualizar la fila', 'status' : status.HTTP_200_OK})
                elif registro == 0 :
                    return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido : {str(e)}")
            return False

class PerfilUsuarioDetail(APIView):
    serializer_class = BasePropiedadesSerializer
    serializer_class_put = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registro = DAOUsuario.devolver_data_usuario(data['id_usuario'])
                if registro == 0 :
                    return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_404_NOT_FOUND})
                serializer = PerfilUsuarioSerializer(registro, many = False)
                return JSONResponse(serializer.data)
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except BaseException as e :
            print(f"Error desconocido : {str(e)}")
            return False
    
    def put(self, request):
        try:
            serializer = self.serializer_class_put(data=request.data)
            if serializer.is_valid():
                data = serializer.data
                registro = DAOUsuario.actualizar_data_usuario(*data.values())
                if registro == 1 :
                    return JSONResponse({'mensaje-success' : 'Se logró actualizar la fila', 'status' : status.HTTP_200_OK})
                elif registro == 0 :
                    return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
            else :
                return JSONResponse({ 'mensaje-error' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except BaseException as e :
            print(f"Error desconocido : {str(e)}")
            return False

from rest_framework.decorators import api_view, permission_classes
import jwt
from django.conf import settings

# def verificar_perfil(token):
#     payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#     usuario = payload.get('id_usuario', '')
#     try:
#         usuario = Usuario.objects.get(id_usuario=usuario)
#         perfil = PerfilesUsuario.objects.filter(id_usuario=usuario.id_usuario)
#     except Usuario.DoesNotExist:
#         return JSONResponse({'error': 'No existe el usuario con el que intentas realizar esta acción.'}, status=status.HTTP_404_NOT_FOUND)
#     return perfil.id_perfil


@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def arrendarPropiedad(request):
    data = request.data
    pk = data.get('id_propiedad')  # Asume que 'pk' es el nombre del campo en los datos del request

    try:
        propiedad = Propiedad.objects.get(pk=pk)
    except Propiedad.DoesNotExist:
        return JSONResponse({'error': 'No existe la propiedad que intentas actualizar.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ActualizarPropiedad(propiedad, data=data)

    if serializer.is_valid():
        # data = serializer.validated_data
        # print(data)
        # estado = Estados.objects.get(pk=data.get('ultimo_estado'))
        # propiedad.ultimo_estado = estado
        serializer.save()
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)
    else: 
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import requests
def header_request_transbank() :
    headers = {
        "Authorization": "Token",
        "Tbk-Api-Key-Id": "597055555532",
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        'Referrer-Policy': 'origin-when-cross-origin',
        } 
    return headers

class TransbankCreate(APIView):
    def post(self, request):
        headers = header_request_transbank()
        data = request.data
        url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
        response = requests.post(url, json=data, headers=headers)
        return JSONResponse(response)

class TransbankCommit(APIView):
    def post(self, request, token_ws):
        headers = header_request_transbank()
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{token_ws}"
        response = requests.put(url, headers=headers)
        return JSONResponse(response)

class TransbankReverseOrCancel(APIView):
    def post(self, request):
        headers = header_request_transbank()
        token_ws = request.data
        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{token_ws}/refunds"
        response = requests.post(url, headers=headers)
        return JSONResponse(response)