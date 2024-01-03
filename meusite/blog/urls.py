from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_post, name='listar_post'),
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    path('post/new/', views.novo_post, name='novo_post'),
    path('post/<int:pk>/edit/', views.edicao_post, name='edicao_post'),
]