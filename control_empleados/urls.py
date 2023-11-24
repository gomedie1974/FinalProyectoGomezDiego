from django.urls import path

from control_empleados.views import (
     crear_sector, listar_sector, buscar_sector, eliminar_sector, editar_sector,   EmpleadoListView, EmpleadoCreateView, EmpleadoDetailView, EmpleadoUpdateView, EmpleadoDeleteView, listar_jefe, crear_jefe, eliminar_jefe, editar_jefe, buscar_jefe, acerca_de_mi
)

urlpatterns = [
      path('acerca-de-mi/', acerca_de_mi, name='acerca_de_mi'),
      #SECTORES 
      path('sector/', listar_sector, name='listar_sector'),
      path('crear-sector/', crear_sector, name='crear_sector'),
      path('buscar-sector/', buscar_sector, name='buscar_sector'),
      path('eliminar-sector/<int:id>/', eliminar_sector, name='eliminar_sector'),
      path('editar-sector/<int:id>/', editar_sector, name='editar_sector'),
 
      #JEFES
      path('jefe/', listar_jefe, name='listar_jefe'),
      path('crear-jefe/', crear_jefe, name='crear_jefe'),
      path('eliminar-jefe/<int:id>/', eliminar_jefe, name='eliminar_jefe'),
      path('editar-jefe/<int:id>/', editar_jefe, name='editar_jefe'),
      path('buscar-jefe/', buscar_jefe, name='buscar_jefe'),


 
      #EMPLEADOS  
      path('empleados/', EmpleadoListView.as_view(), name='listar_empleados'),
      path('empleados/<int:pk>/', EmpleadoDetailView.as_view(), name='ver_empleados'), 
      path('crear-empleado/', EmpleadoCreateView.as_view(), name='crear-empleado'),
      path('editar-empleado/<int:pk>/', EmpleadoUpdateView.as_view(), name='editar-empleado'),
      path('eliminar-empleado/<int:pk>/', EmpleadoDeleteView.as_view(), name='eliminar-empleado'),
      

]
 
