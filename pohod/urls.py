from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIAURL, documentroot=settings.MEDIA_ROOT)
