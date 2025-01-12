from django.shortcuts import render, get_object_or_404

from .models import Catalog


def pohod_list(request):
    catalog = Catalog.objects.filter(is_published=True)  # Получаем только опубликованные походы
    template = 'catalog/pohod_list.html'
    context = {'catalog': catalog}
    return render(request, template, context)


def pohod_detail(request, pk):
    catalog = get_object_or_404(Catalog, id=pk)  # Загружаем поход по ID
    template = 'catalog/pohod_detail.html'
    context = {'catalog': catalog}  # Передаем единственный элемент в контекст
    return render(request, template, context)
