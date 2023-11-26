from django.urls import path
from .views import lista_clientes

urlpatterns = [
    path('lista/', lista_clientes, name='lista_clientes'),
]
