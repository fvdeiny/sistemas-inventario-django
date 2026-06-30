
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- IMPORTANTE
from inventory.views import lista_productos ,registrar_movimiento, api_lista_productos  # importamos las vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', lista_productos, name = 'lista_productos' ), # Nueva ruta 
    path('productos/movimiento/', registrar_movimiento, name='registrar_movimiento'),
    path('api/productos/', api_lista_productos, name='api_lista_productos'),
    path('api/token/', obtain_auth_token, name='api_token'),  # <-- NUEVO ENDPOINT DE SEGURIDAD
]
