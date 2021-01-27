from django.urls import path
from .import views
urlpatterns = [
	path('',views.HomeView.as_view(),name='home'),
	path('detail/<slug:pk>/',views.DetailHomeView.as_view(),name='detail'),
	]