from django.contrib import admin
from .models import Places, PapularDestinations, Trips, Testimonials, Subscribers

# Register your models here.
admin.site.register(Places)
admin.site.register(PapularDestinations)
admin.site.register(Testimonials)
admin.site.register(Trips)
admin.site.register(Subscribers)