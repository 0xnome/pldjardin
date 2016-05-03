from django.contrib import admin

from .models import Jardin, Adresse, Lopin, Plante, Actualite, PlanteInfo

# Register your models here.


admin.site.register(Jardin)
admin.site.register(Adresse)
admin.site.register(Lopin)
admin.site.register(Plante)
admin.site.register(Actualite)
admin.site.register(PlanteInfo)
