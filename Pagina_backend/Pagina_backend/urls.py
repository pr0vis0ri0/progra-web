from django.contrib import admin
from django.urls import path, include
from backend import viewsets, views
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Creamos un router y registramos nuestro viewset

# router = DefaultRouter()
# router.register("region", viewsets.RegionViewSet, basename='Region')
# router.register('comuna', viewsets.ComunaViewSet, basename='Comuna')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('backend.urls')),
    # path('', include(router.urls)),
    # path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/schema/', SpectacularAPIView.as_view(),name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]