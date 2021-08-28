from django.contrib import admin

# Register your models here.
from .models import client, transport
admin.site.register(transport)
admin.site.register(client)