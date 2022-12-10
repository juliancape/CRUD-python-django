from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('edicionCurso/', views.edicionCurso)
]