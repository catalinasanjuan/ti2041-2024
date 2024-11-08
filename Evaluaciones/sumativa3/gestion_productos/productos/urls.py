from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import custom_login_view

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("login/", custom_login_view, name="login"),
    path('productos/', views.index, name='index'),
    path('registro/', views.registro_producto, name='registro_producto'),
    path('resultado/<int:producto_id>/', views.resultado, name='resultado'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='login.html')),  # Redirige la raíz al login
]
