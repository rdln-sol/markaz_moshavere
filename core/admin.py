from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(Psychologist)
admin.site.register(Appointment)
admin.site.register(Dossier)
admin.site.register(Treatment_Plan)
admin.site.register(Reception)
admin.site.register(Profit)
admin.site.register(Conditions)
admin.site.register(Medication)