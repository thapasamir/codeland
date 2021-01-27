from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import cateogies,section
# Create your views here.

class HomeView(ListView):

	template_name = 'home.html'
	model = cateogies
	context_object_name = 'cateo'

class DetailHomeView(DetailView):
	model = cateogies
	template_name = 'home.html'
	context_object_name = 'cateogies'
	slug_url_kwarg = 'the_slug'
	slug_field = 'slug'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['passing'] = section.objects.all()
		return context

class SectionView(ListView):
	model = section
	context_object_name = 'section'
	template_name = 'home.html'
