# Generated by Django 4.2.4 on 2023-08-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_taches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liste_taches',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date et heure de création de la tâche'),
        ),
    ]
