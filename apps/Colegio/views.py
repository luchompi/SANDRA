from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sede,Curso
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .forms import sedeForm

class SedeListView(ListView):
    model = Sede
    template_name = "Colegio/Sede/index.html"

class SedeCreateView(CreateView):
    model = Sede
    form=sedeForm
    fields = ['nombre','direccion','telefono','correo']
    success_url='/colegio/sedes/'
    template_name = "Colegio/Sede/create.html"