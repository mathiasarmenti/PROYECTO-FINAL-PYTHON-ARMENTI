from django.shortcuts import render, redirect
from aplicacion.models import Clientes, Producto
from aplicacion import forms
# Create your views here.


def inicio(request):
    return render(request, 'plantillas/app/base.html')


def clientes(request):
    if request.method == 'POST':
        form = forms.ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = forms.ClientesForm()
    return render(request, 'plantillas/app/clientes.html', {'form': form})


def productos(request):
    if request.method == 'POST':
        form = forms.ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = forms.ProductosForm()
    return render(request, 'plantillas/app/producto.html', {'form': form})

def busqueda(request):
    if 'q' in request.GET:
        query = request.GET['q']
        clientes = Clientes.objects.filter(nombre__icontains=query)
        productos = Producto.objects.filter(nombre__icontains=query)
        return render(request, 'plantillas/app/busqueda.html', {'clientes': clientes, 'productos': productos})
    return render(request, 'plantillas/app/busqueda.html')