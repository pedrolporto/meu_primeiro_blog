from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_post, name='listar_post'),
]