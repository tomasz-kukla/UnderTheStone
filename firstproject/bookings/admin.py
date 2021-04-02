from django.contrib import admin

from .models import Reservation, Table, Section

admin.site.register(Reservation)
admin.site.register(Table)
admin.site.register(Section)
