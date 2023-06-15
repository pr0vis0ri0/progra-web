from .models import Region, Comuna
from .serializers import RegionSerializer, ComunaSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from .jsonresponse import JSONResponse

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ComunaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

    @action(
            detail=False, 
            methods=['POST'],
            url_path=r'filtroRegiones/(?P<id_region>\d+)')
    def filtroRegiones(self, request, id_region):
        queryset = Comuna.objects.filter(id_region = id_region)
        serializer_class = ComunaSerializer(queryset, many = True)
        return JSONResponse(serializer_class.data)