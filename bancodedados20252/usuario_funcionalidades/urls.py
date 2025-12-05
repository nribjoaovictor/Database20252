from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_usuario, name='home'), 

    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    
    path('chamados/', views.listar_chamados, name='listar_chamados'),
    path('chamados/novo/', views.criar_chamado, name='criar_chamado'),
    path('chamados/editar/<int:id>/', views.editar_chamado, name='editar_chamado'),
    path('chamados/excluir/<int:id>/', views.excluir_chamado, name='excluir_chamado'),
]