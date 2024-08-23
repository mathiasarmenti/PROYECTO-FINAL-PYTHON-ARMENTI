from django import forms
from aplicacion import views


class ClientesForm(forms.ModelForm):
    class Meta:
        model = views.Clientes
        fields = '__all__'

class ProductosForm(forms.ModelForm):
    class Meta:
        model = views.Producto
        fields = '__all__'