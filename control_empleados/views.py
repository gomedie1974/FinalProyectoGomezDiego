from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from control_empleados.models import Empleado, Sector
from django.urls import reverse, reverse_lazy
from control_empleados.forms import SectorFormulario



# Create your views here.

#CLASES BASADAS EN VISTAS

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


#CLASES BASADAS EN CLASES
#EMPLEADOS
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'control_empleados/listar_empleados.html'
class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = ('apellido', 'nombre', 'email', 'telefono', 'dni', 'fecha_nacimiento') 
    success_url = reverse_lazy ('listar_empleados.html')
class EmpleadoDetailView(DetailView):
    model = Empleado
    success_url = reverse_lazy ('listar_empleados.html')
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ('apellido', 'nombre', 'email', 'telefono', 'dni', 'fecha_nacimiento') 
    success_url = reverse_lazy ('listar_empleados.html')
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy ('listar_empleados.html')


 
 