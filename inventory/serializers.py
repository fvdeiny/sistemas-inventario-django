from rest_framework import serializers
from . models import Producto

class productoserializers(serializers.ModelSerializer):
    # Traemos el nombre de la categoría en lugar de su ID numérico para que el JSON sea descriptivo
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        # Los campos que convertiremos en formato JSON
        fields = ['sku', 'nombre', 'precio', 'stock', 'categoria_nombre']