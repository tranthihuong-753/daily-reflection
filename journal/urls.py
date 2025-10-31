from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bieton/', views.bieton, name='bieton'),
    path('muonlam/', views.muonlam, name='muonlam'),
    path('baihoc/', views.baihoc, name='baihoc'),
]
