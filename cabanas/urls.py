from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cabana/<int:id>/', views.detalle_cabana, name='detalle_cabana'),
    path('opinion/agregar/<int:id>/', views.agregar_opinion, name='agregar_opinion'),
    path('opinion/editar/<int:id>/', views.editar_opinion, name='editar_opinion'),
    path('opinion/eliminar/<int:id>/', views.eliminar_opinion, name='eliminar_opinion'),

]
