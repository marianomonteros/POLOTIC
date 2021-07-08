from django.urls import path
from . import views

app_name = "JAGUARETE_V1"
urlpatterns = [

    path('', views.index,name="index"),
    path('acerca_de', views.acerca_de,name="acerca_de"),
    path('carrito', views.carrito,name="carrito"),
    path('login', views.login,name="login"),
    path('producto', views.producto,name="producto"),
    path('registro', views.registro,name="registro"),
    path('result_bus', views.result_bus,name="result_bus"),
    path('agregartarea', views.agregartarea,name="agregartarea")
    
]