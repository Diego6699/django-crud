from django.contrib import admin
from django.urls import include, path

from .views import delete, editar, home, salvar, update

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name = 'update'),
    path('delete/<int:id>', delete, name = 'delete'),
]
