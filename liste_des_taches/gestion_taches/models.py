from django.db import models


class liste_taches(models.Model):

    titre = models.fields.CharField(max_length=100)
    auteur = models.fields.CharField(max_length=50)
    active = models.fields.BooleanField(default=True)
    description = models.fields.CharField(max_length=500)
    date_creation = models.fields.DateTimeField(
        verbose_name="Date et heure de création de la tâche"
        )
    date_cloture = models.fields.DateTimeField(
        verbose_name='Date et heure de cloture de la tâche',
        default=None
    )
    