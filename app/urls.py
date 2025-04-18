from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Main index page
    path('about/', views.index, name='about'),     # All point to index.html
    path('services/', views.index, name='services'),
    path('gallery/', views.index, name='gallery'),
    path('contact/', views.index, name='contact'),
]
