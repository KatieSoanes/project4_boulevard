from django.contrib import admin

from .models import Restaurant,Reservation, Booking

admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Booking)
