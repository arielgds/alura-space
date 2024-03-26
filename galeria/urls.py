from django.contrib import admin
from django.urls import path, include
from galeria.views import buscar,index,imagem


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('', include('galeria.urls')),
    path('buscar', buscar, name='buscar'),
]