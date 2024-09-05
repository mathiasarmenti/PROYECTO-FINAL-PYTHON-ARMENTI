from aplicacion import views
from aplicacion import views_clases
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('about/', views.about, name='about'),
    path('leerclientes/', views.leerclientes, name= 'leerclientes'), 
    path('eliminarcliente/<cliente_nombre>/', views.eliminarcliente, name= 'eliminarcliente'),

]


urls_vistas_clases = [
    path('clases/list/', views_clases.ProductoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views_clases.ProductoDetalle.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.ProductoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views_clases.ProductoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views_clases.ProductoDeleteView.as_view(), name='Delete')
]

urlpatterns += urls_vistas_clases