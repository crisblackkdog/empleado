from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#model
from .models import Empleado

from .forms import EmpleadoForm
# Create your views here.

# 1.- listar todos los empleados de la empresa
class InicioView(TemplateView):
    """pagina de inicio"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'id'
    context_object_name = 'empleado'
    # context_object_name = 'lista_empleados'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        print('lista resultado: ', lista)
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/list_empleados.html'
    paginate_by = 10
    model = Empleado
    ordering = 'id'
    context_object_name = 'empleados'

# 2.- listar todos los empleados que perteneces a un area de la empresa

class ListByAreaEmpleado(ListView):
    """lista empleados de un area"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    def  get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
        departamento__short_name = area 
        )
        return lista

class ListEmpleadosByKword(ListView):
    """lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        print('lista resultado: ', lista)
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        empleado = Empleado.objects.get(
        first_name = palabra_clave
        )
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context


class SuccesView(TemplateView):
    template_name = "persona/succes.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:inicio')

    def form_valid(self, form):
        #logica del codigo
        empleado = form.save(commit=False)
        empleado.full_name =empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html" 
    model = Empleado
    fields = ['first_name',
              'last_name',
              'job',
              'departamento',
              'habilidades',
              'avatar',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete-empleado.html"
    success_url = reverse_lazy('persona_app:empleados_admin')