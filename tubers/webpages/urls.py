from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='webpages.home'),
    path('about/', views.about, name='webpages.about'),
    path('services/', views.services, name='webpages.services'),
    path('contact/', views.contact, name='webpages.contact'),
] 