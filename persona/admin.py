from django.contrib import admin
from .models import Persona, PersonaAdmin

admin.site.register(Persona),
admin.site.register(Persona, PersonaAdmin)
