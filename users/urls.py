from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', views.cerrar_sesion , name="Logout"),
    path('edit/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_pass/', views.CambiarContrasenia.as_view(), name="Cambiar_pass"),
    
    
]
    