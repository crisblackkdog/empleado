from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name ='inicio'),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name = 'empleados_all'
    ),
    path(
        'lista-empleado-admin/', 
        views.ListaEmpleadosAdmin.as_view(),
        name = 'empleados_admin'
    ),
    path('listar-by-area/<shortname>', views.ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('listar-by-area/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>',
          views.EmpleadoDetailView.as_view(),
          name='empleado_detail'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name = 'empleado_add'
    ),
    path('succes/', views.SuccesView.as_view(), name = 'correcto'),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name = 'modificar-empleado'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name = 'eliminar-empleado'),

]


