from django.contrib import admin
from .models import Advisor,Booking

# Registering to admin panel
admin.site.register(Advisor)
admin.site.register(Booking)
