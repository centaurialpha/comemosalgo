from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class RegistroUsuario(CreateView):
    model = User
    template_name = "registrar.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('index:index')


