from django.contrib import admin

from .models import formatt, bill, item, temp, order
admin.site.register(formatt)
admin.site.register(bill)
admin.site.register(item)
admin.site.register(order)
admin.site.register(temp)