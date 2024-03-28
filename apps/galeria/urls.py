from django.urls import path, include
from apps.galeria.views import buscar,index,imagem, nova_imagem, editar_imagem, deletar_imagem, filtro


urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova_imagem', nova_imagem, name='nova_imagem'),
    path('editar_imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar_imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
    

]