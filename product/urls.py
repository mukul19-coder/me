from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product.views import addproduct, product_list

urlpatterns = [
    path('addproduct/', addproduct, name='addproduct'),
    path('list/', product_list, name='list'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
