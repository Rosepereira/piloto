from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('ajuda/', views.ajuda, name="ajuda"),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('dia/<int:numero>/', views.diasemana, name='diasemana'),
    path('produtos/', views.produtos, name="produtos"),
    path('produtos/form/', views.form_produto, name="form_produto"),
    path('produtos/detalhes/<int:id>/', views.detalhes_produto, name="detalhes_produto"),
    path('produtos/editar/', views.editar_produto, name="editar_produto"),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name="excluir_produto"),
]  
