from django.shortcuts import render, redirect
from aplicacion.models import Clientes, Producto
from aplicacion import forms
from django.contrib.auth.decorators import login_required


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


def about(request):
    return render(request,'plantillas/app/about.html')


@login_required
def leerclientes(request):

      cliente = Clientes.objects.all()

      contexto= {"cliente":cliente} 

      return render(request, 'plantillas/app/leerclientes.html',contexto)

@login_required
def eliminarcliente(request, cliente_nombre):
 
    cliente = Clientes.objects.get(nombre=cliente_nombre)
    cliente.delete()
 
    cliente = Clientes.objects.all()  
 
    contexto = {"cliente": cliente}
 
    return render(request, 'plantillas/app/leerclientes.html', contexto)


def ClienteFormulario(request):  

    print("Entrando en la vista clienteformulario")  

    if request.method == 'POST':
        print("Solicitud POST recibida")  

        miFormulario = ClienteFormulario(request.POST) 

        if miFormulario.is_valid():
            print("Formulario válido")  
            informacion = miFormulario.cleaned_data
            cliente = Clientes(nombre=informacion['nombre'], apellido=informacion['apellido'])
           
            cliente.save()

            return render(request, 'plantillas/app/padre.html') 
        else:
            print("Formulario no válido") 

    else:
        print("Solicitud GET recibida") 
        miFormulario = ClienteFormulario()

    return render(request, 'plantillas/app/cliente.html', {"miFormulario": miFormulario})



