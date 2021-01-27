from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import cateogies
# Create your views here.

class HomeView(ListView):
	"""This class is used to display home page and render the content from the models(database) dynamically"""
	template_name = 'home.html'
	model = cateogies
	context_object_name = 'cateo'

class DetailHomeView(DetailView):
	model = cateogies
	template_name = 'home.html'
	context_object_name = 'cateogies'


