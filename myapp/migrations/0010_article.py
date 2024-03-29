# Generated by Django 4.2 on 2023-05-16 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_delete_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=255)),
                ("subtitre", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="photos/%y/%m/%d")),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("General", "General"),
                            ("Developement", "Developement"),
                            ("Ai", "Ai"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("date_creation", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
