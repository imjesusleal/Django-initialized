from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('<int:Directores_id>/', views.directores, name='directores'),
    path('<int:Peliculas_id>/', views.peliculas, name = 'peliculas')
]