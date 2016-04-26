from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from apps.gensdujardin.models import Utilisateur


# Register your models here.
# Define an inline admin descriptor for Utilisateur model
# which acts a bit like a singleton
class UtilisateurInline(admin.StackedInline):
    model = Utilisateur
    can_delete = False
    verbose_name = 'utilisateur'
    verbose_name_plural = 'utilisateurs'


# Define a new User admin
class UtilisateurAdmin(UserAdmin):
    inlines = (UtilisateurInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UtilisateurAdmin)
