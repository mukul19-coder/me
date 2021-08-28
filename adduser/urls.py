from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from adduser.views import add_data, addclient, addtransport, beneficiary

urlpatterns = [
    path('add/', add_data, name='add_beneficiary'),
    path('addclient/', addclient, name='addclient'),
    path('list/', beneficiary, name='beneficiary'),
    path('addtransport/', addtransport, name='addtransport'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
