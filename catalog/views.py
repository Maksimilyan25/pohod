from django.views.generic import ListView, DetailView

from .models import Catalog


class PohodListView(ListView):
    model = Catalog  # Модель каталог с полями.
    template_name = 'catalog/pohod_list.html'
    context_object_name = 'catalog'

    def get_queryset(self):
        return Catalog.objects.filter(is_published=True)


class PohodDetailView(DetailView):
    model = Catalog  # Модель каталог с полями.
    template_name = 'catalog/pohod_detail.html'  # Путь к вашему шаблону
    context_object_name = 'catalog'  # Имя переменной в шаблоне
