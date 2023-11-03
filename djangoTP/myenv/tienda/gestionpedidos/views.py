from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionpedidos.forms import FormularioContacto

def busqueda_productos(request):
    return render (request,"busqueda_productos.html")
def pagina_de_inicio(request):
    return render (request, 'pagina_de_inicio.html' )
def buscar (request):
    if request.GET["prod"]:
        # mensaje='Articulo buscado: %r'%request.GET["prod"]
        producto=request.GET["prod"]
        
        if len(producto)>20:
           mensaje="Texto demasiado largo"
        else: 
          
            art=articulos.objects.filter(nombre__icontains=producto)
            return render(request,"resultados_busqueda.html",{"articulos":art, "query":producto})
    else:
        mensaje='No ha introducido nada'
    return HttpResponse(mensaje)

"""
 def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["danielspinella10@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"gracias.html")
    return render(request,"contacto.html") """
def contacto(request):
    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infform=miFormulario.cleaned_data
            send_mail(infform['asunto'],infform['mensaje'],
            infform.get('email',''),['danielspinella10@gmail.com'],)
            return render(request,"gracias.html")
    else:
        miFormulario=FormularioContacto()
    return render(request,"formulario_contacto.html", {"form":miFormulario})
