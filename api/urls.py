from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('lista-receitas/', views.listaReceitas, name='lista-receitas'),
    path('detalhe-receita/<str:pk>', views.detalheReceita, name='detalhe-receita'),
    path('cria-receita/', views.criaReceita, name='cria-receita'),
    path('atualiza-receita/<str:pk>', views.atualizaReceita, name='atualiza-receita'),
    path('deleta-receita/<str:pk>', views.deletaReceita, name='deleta-receita'),
]