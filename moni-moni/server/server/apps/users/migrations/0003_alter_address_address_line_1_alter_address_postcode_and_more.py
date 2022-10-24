# Generated by Django 4.1.2 on 2022-10-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_address_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="address_line_1",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="address",
            name="postcode",
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name="address",
            name="town_city",
            field=models.CharField(max_length=150),
        ),
    ]