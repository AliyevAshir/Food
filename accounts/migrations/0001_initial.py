# Generated by Django 4.2.11 on 2024-10-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlackListedIPAddresses",
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
                ("ip_address", models.GenericIPAddressField()),
            ],
            options={
                "verbose_name": "Black Listed IP Address",
                "verbose_name_plural": "Black Listed IP Addresses",
            },
        ),
    ]
