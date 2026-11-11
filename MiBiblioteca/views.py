from django.shortcuts import render, get_object_or_404
from .models import Libro

# Create your views here.
def lista_libros(request):
    libros = Libro.objects.all().order_by('titulo')
    return render(request, 'mibiblioteca/lista_libros.html', {'libros':libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'mibiblioteca/detalle_libro.html', {'libro':libro})