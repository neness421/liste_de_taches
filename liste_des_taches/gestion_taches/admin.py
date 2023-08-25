from django.contrib import admin
from gestion_taches.models import liste_taches

class ListeTachesAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur')

admin.site.register(liste_taches, ListeTachesAdmin)
# Register your models here.
