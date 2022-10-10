from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app1.views import list_item, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_item, name='item_list'),
    path('search/', search, name='search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
