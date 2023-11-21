from django.urls import path

from control_empleados.views import listar_empleados, crear_sector, listar_sector, buscar_sector, eliminar_sector, editar_sector

urlpatterns = [
      #EMPLEADOS  
      path('empleados/', listar_empleados, name='listar_empleados'),
      
      #SECTORES 
      path('sector/', listar_sector, name='listar_sector'),
      path('crear-sector/', crear_sector, name='crear_sector'),
      path('buscar-sector/', buscar_sector, name='buscar_sector'),
      path('eliminar-sector/<int:id>/', eliminar_sector, name='eliminar_sector'),
      path('editar-sector/<int:id>/', editar_sector, name='editar_sector'),

]
 
