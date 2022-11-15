from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registro/',views.registroPersonas,name='registro'),
    path('registroMascotas/',views.registroMascotas,name='registromascotas'),
    path('verPersonas/',views.verPersonas,name='verPersonas'),
    path('verMascotas/',views.verMascotas,name='verMascotas'),
    path('borrar/<int:id>',views.borrar,name='borrar'),
    path('borrarMascota/<int:id>',views.borrarMascota,name='borrarMascota'),
    path('editar/<int:id>',views.editar,name='editar'),
    path('editarMascotas/<int:id>',views.editarMascota,name='editarMascota'),
]