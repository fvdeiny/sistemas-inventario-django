from django import forms
from .models import MovimientoInventario

class MovimientoInventarioForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        # Indicamos qué campos queremos mostrar en la página web
        fields = ['producto', 'tipo', 'cantidad', 'motivo']
        
        # Le agregamos estilos de Bootstrap a los campos para que se vean profesionales
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Compra de proveedor o Despacho a cliente'}),
        }