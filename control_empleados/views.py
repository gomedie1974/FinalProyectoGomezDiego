from django.shortcuts import render

# Create your views here.
def listar_empleados(request):
    contexto = {
        "empleados": [
        {"nombre": "Emanuel", "apellido": "Dautel"},
        {"nombre": "Manuel", "apellido": "Gomez"},
        {"nombre": "Ivan", "apellido": "Tomasevich"},
        {"nombre": "Carlos", "apellido": "Perez"},
        ]
    }
    http_response = render(
        request=request,
        template_name='control_empleados/listar_empleados.html',
        context=contexto,
    )
    return http_response