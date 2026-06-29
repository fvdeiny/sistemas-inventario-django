from django.shortcuts import render, redirect
from. models import Producto
from .forms import MovimientoInventarioForm  # <-- Importamos el formulario
from django.contrib import messages         # <-- Para mostrar mensajes de éxito o error

# Create your views here.
def lista_productos(request):
    # Traemos todo los productos desde postgresql usando el orm
    productos = Producto.objects.all().order_by('nombre')
    
# Pasamos los datos al archivo html  a traves de un contexto
    return render(request, 'inventory/lista_productos.html', {'productos':productos})

#  NUEVA VISTA PARA EL FORMULARIO 
def registrar_movimiento(request):
    if request.method == 'POST':
        form = MovimientoInventarioForm(request.POST)
        if form.is_valid():
            try:
                # El método save() del formulario ejecuta el clean() y save() de nuestro modelo automáticamente
                form.save()
                messages.success(request, "¡Movimiento registrado y stock actualizado con éxito!")
                return redirect('lista_productos') # Nos manda de vuelta a la tabla
            except Exception as e:
                # Si el modelo lanza la validación de "Stock insuficiente", la atrapamos aquí
                # Quitamos los corchetes o diccionarios para mostrar solo el texto limpio
                error_msg = e.message_dict.get('cantidad', [str(e)])[0] if hasattr(e, 'message_dict') else str(e)
                form.add_error('cantidad', error_msg)
    else:
        form = MovimientoInventarioForm()
        
    return render(request, 'inventory/registrar_movimiento.html', {'form': form})




from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import productoserializers  # <-- Importamos tu nuevo serializador

@api_view(['GET']) # Restringimos el endpoint para que solo acepte peticiones GET de lectura
def api_lista_productos(request):
    """
    Endpoint que devuelve el stock de todos los productos en formato JSON
    """
    productos = Producto.objects.all().order_by('nombre')
    # Transformamos el QuerySet de la base de datos a estructuras nativas de Python/JSON
    serializer = productoserializers(productos, many=True)
    return Response(serializer.data)