from django.contrib import admin

# Register your models here.
from control_empleados.models import Empleado, Jefe, Sector 
 
from perfiles.models import Avatar

admin.site.register(Empleado)
admin.site.register(Jefe)
admin.site.register(Sector)
admin.site.register(Avatar)
