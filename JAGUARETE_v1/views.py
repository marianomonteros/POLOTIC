from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django import forms
from django.urls import reverse
# Create your views here.


class FormAltaTarea(forms.Form):
    tarea = forms.CharField(label="Nuevo producto")


def acerca_de(request):
    return render(request, "jaguarete/acerca_de.html")


def carrito(request):
    return render(request, "jaguarete/carrito.html")


def login(request):
    return render(request, "jaguarete/login.html")


def registro(request):
    return render(request, "jaguarete/registro.html")


def producto(request):
    if "tareas" not in request.session:
        request.session["tareas"] = []
    return render(request, "jaguarete/producto.html", {
        'tareas': request.session["tareas"]
    })


def index(request):
    return render(request, "jaguarete/index.html")


def result_bus(request):
    return render(request, "jaguarete/result_bus.html")


def agregartarea(request):
    if request.method == "POST":
        form = FormAltaTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            request.session["tareas"] += [tarea]
            return HttpResponseRedirect(reverse("JAGUARETE_V1:producto"))
        else:
            return render(request, "jaguarete/agregartarea.html")
    else:
        return render(request, "jaguarete/agregartarea.html")
