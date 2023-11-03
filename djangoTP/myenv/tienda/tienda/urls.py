
from django.contrib import admin
from django.urls import path
from gestionpedidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_productos/', views.busqueda_productos),
    path('', views.pagina_de_inicio),
    path('buscar/', views.buscar),
    path('contacto/', views.contacto),
]
