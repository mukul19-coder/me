from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bill.views import generate, additem, clearlist, delitem, cancel, render_pdf_view, step2, render_bill, final_step

urlpatterns = [
    path('generate/', generate, name='generate'),
    path('additem/', additem, name='additem'),
    path('cancel/', cancel, name='cancel'),
    path('delitem/', delitem, name='delitem'),
    path('render_bill/', render_bill, name='render_bill'),
    path('final_step/', final_step, name='final_step'),
    path('clearlist/', clearlist, name='clearlist'),
    path('step2/', step2, name='step2'),
    path('render_pdf_view/', render_pdf_view, name='render_pdf_view'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
