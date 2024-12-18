from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('productos/', views.index, name='index'),
    path('registro/', views.registro_producto, name='registro'),
    path('resultado/<int:producto_id>/', views.resultado, name='resultado'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='login.html')),  # Redirige la raíz al login
]
