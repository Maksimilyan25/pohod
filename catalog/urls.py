from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.PohodListView.as_view(), name='pohod_list'),
    path('<int:pk>/', views.PohodDetailView.as_view(), name='pohod_detail'),
]
