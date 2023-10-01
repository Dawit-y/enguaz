from django.contrib import admin
from .models import *

admin.site.register(Adminstration)
admin.site.register(Worker)
admin.site.register(Company)
admin.site.register(Ticket)
admin.site.register(Customer)
admin.site.register(Station)

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'driver', 'company', 'is_availaible', 'is_listed']

@admin.register(AvailableBus)
class AvailableBusAdmin(admin.ModelAdmin):
    list_display = ['source', 'destination', 'date']


@admin.register(Seat)
class Seat(admin.ModelAdmin):
    list_display = ['seat_number', 'bus']