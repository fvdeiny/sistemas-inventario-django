from django.db import models
from django.core.exceptions import ValidationError  # <-- Esto es clave

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock})"

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('INGRESO', 'Ingreso (Entrada)'),
        ('EGRESO', 'Egreso (Salida)'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.cantidad} unidades de {self.producto.nombre}"

    # 1.  CONTROL DE VALIDACIÓN (Muestra error estético en el formulario)
    def clean(self):
        super().clean()
        
        # Validar cantidad
        if self.cantidad is not None and self.cantidad <= 0:
            raise ValidationError({'cantidad': "La cantidad del movimiento debe ser mayor a cero."})

        # Validar stock disponible
        if self.tipo == 'EGRESO' and self.producto_id and self.cantidad:
            if self.producto.stock < self.cantidad:
                raise ValidationError({
                    'cantidad': f"Stock insuficiente. Solo quedan {self.producto.stock} unidades de este producto."
                })

    # 2. ⚙️ CONTROL DE EJECUCIÓN (Aplica los cambios a la BD)
    def save(self, *args, **kwargs):
        if self.tipo == 'INGRESO':
            self.producto.stock += self.cantidad
        elif self.tipo == 'EGRESO':
            self.producto.stock -= self.cantidad

        # Guarda el stock actualizado en el producto
        self.producto.save()
        
        # Guarda el movimiento de inventario de forma normal
        super().save(*args, **kwargs)