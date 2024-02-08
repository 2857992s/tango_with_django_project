from django.urls import path 
from rango import views

app_name = 'rango'

urlpatterns = [
    path(r'index.php', views.index, name='index'),
    path(r'index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

