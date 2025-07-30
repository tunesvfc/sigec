from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeUsuarioView, CreateClienteView, CreateTecnicoView

app_name = 'usuario'

urlpatterns = [
    path('home/', HomeUsuarioView.as_view(), name='home'),
    path('login', auth_views.LoginView.as_view(template_name = 'form_login.html',), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('create/cliente', CreateClienteView.as_view(), name='create-cliente'),
    path('create/tecnico', CreateTecnicoView.as_view(), name='create-tecnico'),
]
