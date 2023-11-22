from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from control_empleados.models import Empleado, Sector, Jefe
from django.urls import reverse, reverse_lazy
from control_empleados.forms import SectorFormulario, JefeFormulario



# Create your views here.

#CLASES BASADAS EN VISTAS

#JEFES
def listar_jefe(request):
    contexto = {
        'jefe': Jefe.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_empleados/listar_jefe.html',
        context=contexto,
    )
    return http_response

@login_required
def crear_jefe(request):
   if request.method == "POST":
       formulario = JefeFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           apellido = data["apellido"]
           dni = data["dni"]
           jefe = Jefe(nombre=nombre, apellido=apellido,dni=dni, creador=request.user)  # lo crean solo en RAM
           jefe.save()  # Lo guardan en la Base de datos

           url_exitosa = reverse('listar_jefe')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = JefeFormulario()
   http_response = render(
        request=request,
        template_name='control_empleados/formulario_jefe.html',
        context={'formulario': formulario}
   )
   return http_response

@login_required
def eliminar_jefe(request, id):
   jefe = Jefe.objects.get(id=id)
   if request.method == "POST":
       jefe.delete()
       url_exitosa = reverse('listar_jefe')
       return redirect(url_exitosa)

@login_required
def editar_jefe(request, id):
   jefe = Jefe.objects.get(id=id)
   if request.method == "POST":
       formulario = JefeFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           jefe.nombre = data['nombre']
           jefe.apellido = data['apellido']
           jefe.dni = data['dni']
           jefe.email = data['email']
           jefe.fecha_nacimiento = data['fecha_nacimiento']
           jefe.profesion = data['profesion']
           jefe.save()
           url_exitosa = reverse('listar_jefe')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': jefe.nombre,
           'apellido': jefe.apellido,
           'dni': jefe.dni,
           'email': jefe.email,
            'fecha_nacimiento' : jefe.fecha_nacimiento,
            'profesion' : jefe.profesion,
       }
       formulario = JefeFormulario(initial=inicial)
   return render(
       request=request,
       template_name='control_empleados/formulario_jefe.html',
       context={'formulario': formulario},
   )

def buscar_jefe(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       #forma de filtro simple
       #sector = Sector.objects.filter(codigo__contains=busqueda)
       #filtro avanzado
       jefe = Jefe.objects.filter(
           Q(nombre__contains=busqueda) | Q(apellido__contains=busqueda)
       )
       contexto = {
           "jefe": jefe,
       }
       http_response = render(
           request=request,
           template_name='control_empleados/listar_jefe.html',
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
   
@login_required
def eliminar_sector(request, id):
   sector = Sector.objects.get(id=id)
   if request.method == "POST":
       sector.delete()
       url_exitosa = reverse('listar_sector')
       return redirect(url_exitosa)

@login_required
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
class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = ('apellido', 'nombre', 'email', 'telefono', 'dni', 'fecha_nacimiento') 
    success_url = reverse_lazy ('listar_empleados.html')

    #def form_valid(self, form):
     #   self.object = form.save(creador=self.request.user)
      #  return super().form_valid(form)
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    success_url = reverse_lazy ('listar_empleados.html')
class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    fields = ('apellido', 'nombre', 'email', 'telefono', 'dni', 'fecha_nacimiento') 
    success_url = reverse_lazy ('listar_empleados.html')
class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy ('listar_empleados.html')


 
 