from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_post, name='listar_post'),
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
]