# Generated by Django 4.2 on 2023-05-16 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_article_date_creation"),
    ]

    operations = [
        migrations.DeleteModel(name="Article",),
    ]
