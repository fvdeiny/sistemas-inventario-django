"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory.views import lista_productos ,registrar_movimiento, api_lista_productos  # importamos las vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', lista_productos, name = 'lista_productos' ), # Nueva ruta 
    path('productos/movimiento/', registrar_movimiento, name='registrar_movimiento'),
    path('api/productos/', api_lista_productos, name='api_lista_productos'),
]
