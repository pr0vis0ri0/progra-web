from django.http import HttpResponse
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from backend.DAO.DAOPropiedad import DAOPropiedad

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class PropiedadDetail(APIView):
    def get(self, request, id_propiedad = None):
        if id_propiedad is not None :
            registro = DAOPropiedad.get_caracteristicas_propiedad(id_propiedad)
            serializer = ViewCaracteristicasSerializer(registro)
            return JSONResponse(serializer.data)
    
class RegistroPropiedadDetail(APIView):
    serializer_class = RegistroPropiedadSerializer
    def post(self, request, format = None):
        try :
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid() :
                data = serializer.data
                if DAOPropiedad.post_registrar_propiedad(*data.values()):
                    print('llegué aquí??')
                    return JSONResponse('Registro creado.')
                else :
                    return JSONResponse(status.HTTP_400_BAD_REQUEST)
            else :
                return JSONResponse({ 'errores' : serializer.errors, 'status' : status.HTTP_400_BAD_REQUEST})
        except Exception as e :
            print(f"Error desconocido: {str(e)}")
            return False
        
class PropiedadList(APIView):
    def get(self, request):
        registros = DAOPropiedad.get_detalle_propiedades()
        serializer = DetallePropiedadesSerializer(registros, many = True)
        return JSONResponse(serializer.data)