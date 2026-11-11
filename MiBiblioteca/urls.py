from . import views
from django.urls import path

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('libro/<int:pk>', views.detalle_libro, name='detalle_libro'),
]