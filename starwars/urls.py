from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cobranza API TSF",
        default_version='v1',
        description="Cobranza: Microservicio",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('personajes/', include('apps.personajes.urls', namespace='personajes')),
    path('peliculas/', include('apps.peliculas.urls', namespace='peliculas')),
    path('usuarios/', include('apps.users.urls', namespace='usuarios')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-token-auth/', views.obtain_auth_token)
]
