from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from aplicacion.models import Clientes, Producto


def saludo(request):
    return HttpResponse("Bienvenido a la tienda virtual")


def probando_template(request):
    nom = "Mathias"
    ap = "Armenti"
    diccionario = {'nombre': nom, 'apellido': ap}

    # # Abrimos el archivo html
    # mi_html = open('./entrega/plantillas/template1.html')

    # # Creamos el template haciendo uso de la clase Template
    # plantilla = Template(mi_html.read())

    # # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    # mi_html.close()

    # # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    # mi_contexto = Context()

    # # Terminamos de construír el template renderizándolo con su contexto
    # documento = plantilla.render(mi_contexto)
    
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    
    
    return HttpResponse(documento)

def agregar_cliente(request,nom,ap):
    cliente = Clientes(nombre=nom, apellido=ap)
    cliente.save()
    return HttpResponse("Acceso cliente")

def agregar_producto(request,cat,prod):
    producto = Producto(categoria=cat, producto=prod)
    producto.save()
    return HttpResponse("Producto agregado")

