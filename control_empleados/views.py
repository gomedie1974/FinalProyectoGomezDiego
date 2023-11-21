from django.shortcuts import render, redirect
from django.db.models import Q
from control_empleados.models import Empleado, Sector 
from django.urls import reverse
from control_empleados.forms import SectorFormulario

# Create your views here.

#EMPLEADOS
def listar_empleados(request):
    contexto = {
        'empleados': Empleado.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_empleados/listar_empleados.html',
        context=contexto,
    )
    return http_response






#SECTORES
def listar_sector(request):
    contexto = {
        'sector': Sector.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_empleados/listar_sector.html',
        context=contexto,
    )
    return http_response
 
def crear_sector(request):
   if request.method == "POST":
       formulario = SectorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           codigo = data["codigo"]
           sector = Sector(nombre=nombre, codigo=codigo)  # lo crean solo en RAM
           sector.save()  # Lo guardan en la Base de datos

           url_exitosa = reverse('listar_sector')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = SectorFormulario()
   http_response = render(
        request=request,
        template_name='control_empleados/formulario_sector.html',
        context={'formulario': formulario}
   )
   return http_response

def buscar_sector(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       #forma de filtro simple
       #sector = Sector.objects.filter(codigo__contains=busqueda)
       #filtro avanzado
       sector = Sector.objects.filter(
           Q(nombre__contains=busqueda) | Q(codigo__contains=busqueda)
       )
       contexto = {
           "sector": sector,
       }
       http_response = render(
           request=request,
           template_name='control_empleados/listar_sector.html',
           context=contexto,
       )
       return http_response
   
def eliminar_sector(request, id):
   sector = Sector.objects.get(id=id)
   if request.method == "POST":
       sector.delete()
       url_exitosa = reverse('listar_sector')
       return redirect(url_exitosa)

def editar_sector(request, id):
   sector = Sector.objects.get(id=id)
   if request.method == "POST":
       formulario = SectorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           sector.nombre = data['nombre']
           sector.codigo = data['codigo']
           sector.save()
           url_exitosa = reverse('listar_sector')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': sector.nombre,
           'codigo': sector.codigo,
       }
       formulario = SectorFormulario(initial=inicial)
   return render(
       request=request,
       template_name='control_empleados/formulario_sector.html',
       context={'formulario': formulario},
   )
