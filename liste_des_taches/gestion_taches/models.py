from django.db import models


class liste_taches(models.Model):

    def __str__(self):
        return f'{self.titre}'

    titre = models.fields.CharField(max_length=100)
    auteur = models.fields.CharField(max_length=50)
    active = models.fields.BooleanField(default=True)
    description = models.fields.CharField(max_length=500)
    date_creation = models.DateTimeField(
        verbose_name="Date et heure de création de la tâche",
        auto_now_add=True
        )
    date_cloture = models.DateTimeField(
        verbose_name='Date et heure de cloture de la tâche',
        default=None
    )
    