# Generated by Django 4.1.2 on 2022-10-31 06:28
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalogue", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="payer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="fundingoptions",
            name="fundraiser",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fundraiser_options",
                to="catalogue.fundraiser",
            ),
        ),
    ]
