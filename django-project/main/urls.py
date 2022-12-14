from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
