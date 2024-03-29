# Generated by Django 4.2 on 2023-05-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_alter_prediction_nombre_de_portes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prediction", name="ABS", field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Airbags",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="CD_MP3_Bluetooth",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Camera_de_recul",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Climatisation",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction", name="ESP", field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Jantes_aluminium",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Limiteur_de_vitesse",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Ordinateur_de_bord",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Radar_de_recul",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Regulateur_de_vitesse",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Sieges_cuir",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Systeme_de_navigation_GPS",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Toit_ouvrant",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Verrouillage_centralise_a_distance",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="Vitres_electriques",
            field=models.BooleanField(blank=True),
        ),
    ]
