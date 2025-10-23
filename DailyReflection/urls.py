from django.contrib import admin
from django.urls import path
from journal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('bieton/', views.bieton, name='bieton'),
    path('muonlam/', views.muonlam, name='muonlam'),
    path('baihoc/', views.baihoc, name='baihoc'),
]
