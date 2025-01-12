from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.pohod_list, name='pohod_list'),
    path('<int:pk>/', views.pohod_detail, name='pohod_detail'),
]