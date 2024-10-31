from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.pruebaListView.as_view()),
    path('prueba/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='add'),
    path('resumen-foundation/', views.ResumenFoundationView.as_view(), name='resumen'),
]

