from django.urls import path
from .import views
urlpatterns = [
	path('',views.HomeView.as_view(),name='home'),
	path('detail/<slug:the_slug>/',views.DetailHomeView.as_view(),name='detail'),
	path('detail/<slug:the_slug>/section',views.SectionView.as_view(),name='section'),
	]