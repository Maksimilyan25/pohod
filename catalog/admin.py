from django.contrib import admin

from .models import Catalog


admin.site.empty_value_display = 'Не задано'


class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


admin.site.register(Catalog, CatalogAdmin)

