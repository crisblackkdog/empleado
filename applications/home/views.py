from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from applications.home.forms import PruebaForm
from applications.home.models import Prueba

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'

class pruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['pedro','juan','cristobal','emilio']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/pruebas.html'
    context_object_name = 'lista_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    succes_url = '/'