from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from me.views import home, menu, logout

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('logout/', logout, name='logout'),
    path('admin/', admin.site.urls),
    path('beneficiary/', include('adduser.urls')),
    path('bill/', include('bill.urls')),
    path('product/', include('product.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
