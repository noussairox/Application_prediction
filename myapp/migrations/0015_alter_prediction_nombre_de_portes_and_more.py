# Generated by Django 4.2 on 2023-05-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_alter_prediction_annee_modele"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prediction",
            name="Nombre_de_portes",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Puissance_fiscale",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
