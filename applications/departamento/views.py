from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from applications.persona.models import Empleado

from .models import Departamento
from applications.departamento.forms import NewDepartamentoForm
#Create your views here.



class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"



class NewDepartamentoView(FormView):
    template_name = 'departamento/new_dapartamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'  # Corregido: success_url en lugar de succes_url

    def form_valid(self, form):
        print('****************estamos en form valid*****')
        
        # Crear el departamento
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortName'],
        )
        depa.save()

        # Crear el empleado
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )

        return super(NewDepartamentoView, self).form_valid(form)